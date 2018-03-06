

#import the appropriate packages
import pandas as pd
import io
import os, sys

def fsl2tsv(subjID, session, task, run, tsv_directory, file_list, condition_list):

    ##########################
    ##PURPOSE: This function takes as input a list of FSL EV files and outputs a single
    ##         BIDS-format .tsv file.
    ##
    ##INPUT:
    ##       subjID: string containing the BIDS subject ID (i.e. what comes after "sub-")
    ##       session: string containing the BIDS session (i.e. what comes after "ses-")
    ##       task: string containing the BIDS task name (i.e. what comes after "task-")
    ##       run: string containing the BIDS run identifier (i.e. what comes after "run-")
    ##       tsv_directory: path into which to write the output .tsv file
    ##       file_list: list of strings containing the full paths/names of the input
    ##                  FSL EV files to be combined into the output .tsv file
    ##       condition_list: list of condition labels (one per input EV file) to be used
    ##                       in the output .tsv file
    ##
    ##OUTPUT: a single .tsv file containing 3 columns: onset, duration, trial_type. The
    ##        file will contain one header line followed by one row per line in each EV.
    ##        The values in trial_type will be taken from the elements in "condition_list".
    ##        The condition onset and duration values will be taken directly from the input
    ##       EV files. The name of the output file will be in BIDS format, generated from
    ##        the other input variable strings.
    ##
    ##AUTHORS:
    ##          Leonard Faul and John Graner, Duke University, 2018
    ##########################

    print('----STARTING fsl2tsv----')

    #Make sure the file list and the label list are the same length
    if len(file_list) != len(condition_list):
        print('Number of files passed is not equal to the number of condition labels passed!')
        print('EXITTING!')
        sys.exit()

    #Create dataframe for appended files
    appended_data = pd.DataFrame()

    #For each EV: define column names, add 'trial_type' by using EV file name, and append to dataframe
    for file, label in zip(file_list, condition_list):
        print('Reading input_file: '+str(file))
        data = pd.read_csv(file, sep='\t', names = ['onset', 'duration', 'on/off'], engine='python')
        data['trial_type'] = label
        appended_data = pd.concat([appended_data, data], ignore_index=True)

    #Sort the appended dataframe by 'onset' time
    print('Sorting appended dataframe...')
    df_sorted = appended_data.sort_values(['onset'])

    #Remove 'on/off' column from original EV file
    BIDS_event_tsv = df_sorted.drop('on/off', axis=1)

    #Write output files
    BIDS_event_tsv.to_csv(path_or_buf=os.path.join(tsv_directory, 'sub-'+subjID+'_ses-'+session+'_task-'+task+'_run-'+run+'_events.tsv'), sep='\t', index=False)

    print('----FINISHED fsl2tsv----')



def tsv2fsl(input_file, base_output_dir):

    #############################
    ##THIS FUNCTION ASSUMES YOUR TSV FILE HAS A 'trial_type' COLUMN!
    #############################

    #Check to make sure input file is there
    if not os.path.exists(input_file):
        raise RuntimeError('Input file cannot be found: {}'.format(input_file))

    #Read input file in as a dataframe
    data = pd.read_csv(input_file, sep='\t', engine='python')

    #Create smaller dataframes for each unique value of trial_type
    if 'trial_type' not in data.keys():
        print('Input .tsv file does not contain a trial_type column!')
        print('Input file: {}'.format(input_file))
        raise RuntimeError

    unique_trial_labels = pd.Series.unique(data.trial_type)

    input_name = os.path.split(input_file)[-1]
    input_prefix = os.path.splitext(input_name)[0]

    #Pull the sub ID, ses, etc. from the input file name
    # id_parts = split_tsv_name(os.path.split(input_file)[-1])

    for element in unique_trial_labels:
        sub_data = data.loc[lambda df: df.trial_type==element]

        #Set all the 'trial_type' column values to 1
        sub_data.trial_type = 1

        #Write out a file from the data frame
        output_name = '{input}_fslev-{label}.txt'.format(input=input_prefix, label=element)
        output_file = os.path.join(base_output_dir, output_name)

        print('Writing file: {}'.format(output_file))
        sub_data.to_csv(path_or_buf=output_file, sep='\t', index=False, header=False)


def split_tsv_name(input_file):

    #This function takes a BIDS tsv file name as input and returns the sub,
    #ses, task, and run found in it as a dictionary.

    return_dict = {}

    ##MAKE SURE FILE IS THERE

    file_name = os.path.split(input_file)[-1]
    file_name = file_name[:-4]

    for element in ['sub', 'ses', 'task', 'run']:
        if element in file_name:
            return_dict[element] = file_name.split('{}-'.format(element))[-1].split('_')[0]

    return return_dict


    ###
    # def __write_fsl(condition_name, start_times, durations, output_dir, subid, runid):
    
    # #This function writes out condition files that can be read by FSL
    
    # output_name = '{}_{}_{}_fslconds.txt'.format(subid, runid, condition_name)
    # output_file = os.path.join(output_dir, output_name)
    
    # #Don't look to see if the output file already exists; just
    # #overwrite it if it does.
    
    # fid = open(output_file, 'w')
    # for count in range(len(start_times)):
    #     line_to_write = '{0:.2f}\t{1:.2f}\t1\n'.format(start_times[count],durations[count])
    #     fid.write(line_to_write)
    # fid.close()
    ###

    ###
    # def __write_tsv(event_list, output_dir, subid, runid):
    
    # #This function writes out an event .tsv file in the BIDS format
    
    # output_name = 'sub-{}_ses-day3_task-emoreg_run-{}_events.tsv'.format(subid, runid)
    # output_file = os.path.join(output_dir, output_name)
    
    # #Don't look to see if the output file already exists; just
    # #overwrite it if it does.
    
    # header_line = 'onset\tduration\ttrial_type\tstim_info\tresponse_time\n'

    # print('Writing file: {}'.format(output_file))

    # fid = open(output_file, 'w')
    # fid.write(header_line)
    # for element in event_list:
    #     try:
    #         line_to_write = '{0:.2f}\t{1:.2f}\t{2}\t{3}\t{4:.2f}\n'.format(element[0],element[1],element[2],element[3],element[4])
    #     except:
    #         line_to_write = '{0:.2f}\t{1:.2f}\t{2}\t{3}\t{4}\n'.format(element[0],element[1],element[2],element[3],element[4])
    #     fid.write(line_to_write)
    # fid.close()
    ###

    ###
    # def __create_bids_entries(type_label, start_type, end_type, lines, response_type=[None]):
    
    # #This function gets called once per condition type, creating BIDS .tsv file
    # #entries for one condition at a time. So, there should either be one response entry
    # #for each start entry, or none at all.

    # #lines is a list of lists. Each element of lines has the following:
    # #[type, timefromstart, stimtype, stimdescrip]
    
    # #This function returns start times and durations for a given condition.
    # events_to_keep = []
    
    # for element in lines:
    #     #If the event type is either start_type or end_type, keep it.
    #     if (element[0] in start_type) or (element[0] in end_type) or (element[0] in response_type):
    #         events_to_keep.append(element)

    # #The resulting list of lists should be in chronological order and there
    # #should not be two start_type events or end_type events in a row (this
    # #is dependent on the task code being written to support this).
    # for i in range(len(events_to_keep)):
    #     #If the type values are the same for any sequential entries, something
    #     #is wrong.
    #     if events_to_keep[i][0] == events_to_keep[i-1][0]:
    #         msg = 'Events of identical type found when trying to create condition!'
    #         print(msg)
    #         raise ValueError(msg)
    
    # #Split the list into two: one for start_type and one for end_type
    # start_list = []
    # end_list = []
    # response_list = []
    # for element in events_to_keep:
    #     if element[0] in start_type:
    #         start_list.append(element)
    #     elif element[0] in end_type:
    #         end_list.append(element)
    #     if None not in response_type:
    #         if element[0] in response_type:
    #             response_list.append(element)
    
    # #The three lists need to have the same number of elements
    # if len(start_list) != len(end_list):
    #     msg = 'Number of start_type elements is {} but number of end_type elements is {}!'.format(len(start_list), len(end_list))
    #     print(msg)
    #     raise ValueError(msg)
    # if None not in response_type:
    #     if (len(start_list) != len(response_list)):
    #         msg = 'Number of response_type elements is {} but number of end_type elements is {}!'.format(len(response_list),len(start_list))
    #         print(msg)
    #         raise ValueError(msg)
        
    # #Create list of durations
    # durations = []
    # for i in range(len(start_list)):
    #     durations.append(float(end_list[i][1]) - float(start_list[i][1]))
    
    # #Create list of start times
    # start_times = []
    # for element in start_list:
    #     start_times.append(float(element[1]))

    # #Create list of response times
    # #If the participant didn't respond to something, the entry will be "None"
    # response_times = []
    # #If no response type was passed, just make a list of n/a
    # if None in response_type:
    #     for element in start_list:
    #         response_times.append('n/a')
    # else:
    #     for element in response_list:
    #         response_times.append(element[3])

    # #Create list of descriptions
    # descriptions = []
    # if None in response_type:
    #     for element in start_list:
    #         descriptions.append(element[3].strip())
    # else:
    #     for element in response_list:
    #         descriptions.append(element[2].strip())

    # #Put all the things into a list of lists. Each inner list will be one
    # #entry in the output .tsv file.
    # event_list = []
    # for i in range(len(start_times)):
    #     event_list.append([start_times[i], durations[i], str(type_label), descriptions[i], response_times[i]])

    # return event_list
    ###

    ###
    # all_events = {}

    # #Create file lines for the arrow trials
    # print('Creating arrow event list...')
    # all_events['arrow_event_list'] = __create_bids_entries('arrow', ['negArrowOnset', 'neuArrowOnset'], ['negArrowOffset', 'neuArrowOffset'],
    #                                             all_line_parts, response_type=['negArrowResponse', 'neuArrowResponse'])

    # #Create file lines for negative memory cue words
    # print('Creating negative memory cue event list...')
    # all_events['neg_mem_event_list'] = __create_bids_entries('negMemCue', ['negMemoryOnset'], ['negMemoryOffset'], all_line_parts)

    # #Create file lines for the neutral arousal prompt
    # print('Creating neutral arousal rating event list...')
    # all_events['neu_arate_event_list'] = __create_bids_entries('neuARate', ['neuArousalOnset'], ['neuArousalOffset'], all_line_parts, response_type=['neuArousalResponse'])
    
    # #Put all the event lists together
    # big_list = []
    # for key in all_events.keys():
    #     for element in all_events[key]:
    #         big_list.append(element)

    # #Sort the big list of events
    # big_list_sort = sorted(big_list, key=itemgetter(0))

    # __write_tsv(big_list_sort, output_dir, subid, runid)

    # print('-----Done!-----')
    ###