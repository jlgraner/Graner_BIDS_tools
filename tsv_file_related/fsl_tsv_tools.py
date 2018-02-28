

#import the appropriate packages
import pandas as pd
import io
import os, sys

def fslcond2bids(subjID, session, task, run, TSV_directory, file_list, condition_list):

    ##########################
    #
    #  *argv is a list of EV .txt files for a specific subject, session, task, and run
    #
    #      Example call for sub-01, ses-day1, acquisition, run-01:
    #
    #          EVs = ['.../EV1.txt',
    #                 '.../EV2.txt',
    #                 '.../EV3.txt',
    #                 '.../EV4.txt']
    #
    #          generate('01', '1', 'acq', '01', '.../BIDS_tsv', *EVs)
    #
    #          writes all tsv files (for all subjects) to same directory (BIDS_tsv)
    #
    ##########################

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
    BIDS_event_tsv.to_csv(path_or_buf=os.path.join(TSV_directory, 'sub-'+subjID+'_ses-'+session+'_task-'+task+'_run-'+run+'_events.tsv'), sep='\t', index=False)
