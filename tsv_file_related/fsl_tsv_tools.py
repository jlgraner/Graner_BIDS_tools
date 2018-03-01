

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