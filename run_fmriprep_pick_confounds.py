
import os
import pandas
import fmriprep_pick_confounds as fpc

subs_to_run = [
               'EM0033'
              ]

ses_to_run = ['day3']

runs_to_run = ['01']
# runs_to_run = ['01', '02', '03', '04']

tasks_to_run = ['emoreg']

rows_to_remove = 4

output_suffix = '_final'

confounds_to_include = [
                        'CSF',
                        'WhiteMatter',
                        # # 'GlobalSignal', <- I wouldn't recommend including this.
                        'stdDVARS',
                        # # 'non-stdDVARS',
                        # # 'vx-wisestdDVARS',
                        # 'FramewiseDisplacement',
                        'tCompCor',
                        'aCompCor',
                        # 'Cosine',
                        # 'NonSteadyStateOutlier',
                        'X',
                        'Y',
                        'Z',
                        'RotX',
                        'RotY',
                        'RotZ'
                        # 'AROMA'
                        ]

# confound_file_base_dir = '/mnt/keoki/experiments2/EMERALD/Data/MRI/BIDS/fmriprep/sub-{sub}/ses-{ses}/func/'
confound_file_base_dir = '/mnt/keoki/experiments2/EMERALD/Data/MRI/Test_area/fmri/'
confound_file_base_name = 'sub-{sub}_ses-{ses}_task-{task}_run-{run}_bold_confounds.tsv'


#A new confound file will need to be written for each run of each session of task for each subject
for sub in subs_to_run:
    for ses in ses_to_run:
        for task in tasks_to_run:
            for run in runs_to_run:
                confound_dir = confound_file_base_dir.format(sub=sub, ses=ses)
                confound_name = confound_file_base_name.format(sub=sub, ses=ses, run=run, task=task)
                confound_file = os.path.join(confound_dir, confound_name)

                print('Creating confound file from: {}'.format(confound_file))

                output_name = os.path.split(confound_file)[-1][:-4]+str(output_suffix)
                output_file = os.path.join(confound_file_base_dir, output_name+'.tsv')

                print('Output file name set: {}'.format(output_file))

                if not os.path.exists(confound_file):
                    print('Confound file cannot be found: {}'.format(confound_file))
                else:
                    #Create a list of confound column names to include in the new file
                    include_list = [] #This list will contain the specific names of columns to be included in the output
                    print('Reading input file as data frame...')
                    data = pandas.read_csv(confound_file, sep='\t', engine='python')
                    #Create an empty data frame to fill in
                    new_data = pandas.DataFrame()
                    for element in confounds_to_include:
                        print('Dealing with confound label: {}'.format(element))
                        #Deal with labels with more than one confound column
                        if element in ['tCompCor', 'aCompCor', 'Cosine', 'NonSteadyStateOutlier', 'AROMA']:
                            #Find column header names that contain the label category
                            match_list = fpc.match_columns(data, element)
                            print('Confound label matched with list: {}'.format(match_list))
                            #Add them all to the full list
                            include_list = include_list + match_list
                        #Deal with labels that don't have multiple confound columns
                        else:
                            include_list.append(element)
                            print('Confound label added to inclusion list: {}'.format(element))
                    #Put the columns with the included column labels into the new data frame
                    print('Creating new data frame from name list: {}'.format(include_list))
                    # for name in include_list:
                    #     new_data[name] = data[name]
                    new_data = fpc.add_columns(data, new_data, include_list)
                    #If desired, remove initial entries corresponding to pre-steady-state TRs
                    if rows_to_remove > 0:
                        print('Removing first {} rows from new data frame.'.format(rows_to_remove))
                        new_data = new_data.drop(range(rows_to_remove))
                    #Write the new data frame out as a new confound file
                    print('Writing output file: {}'.format(output_file))
                    new_data.to_csv(path_or_buf=output_file, sep='\t', index=False)
print('Done!')