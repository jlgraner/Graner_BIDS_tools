
import fsl_tsv_tools as ftt
import os

this_env = os.environ

sub = 'EM0038'
session = 'day3'
task = 'emoreg'
run = '03'

input_file_list = [
                   'sub-EM0038_ses-day3_task-emoreg_run-03_events_fslEV-arrowblocks.txt',
                   'sub-EM0038_ses-day3_task-emoreg_run-03_events_fslEV-diststrategycues.txt',
                   'sub-EM0038_ses-day3_task-emoreg_run-03_events_fslEV-negflowstrategycues.txt',
                   'sub-EM0038_ses-day3_task-emoreg_run-03_events_fslEV-negmemorywords.txt',
                   'sub-EM0038_ses-day3_task-emoreg_run-03_events_fslEV-neumemorywords.txt',
                   'sub-EM0038_ses-day3_task-emoreg_run-03_events_fslEV-reapstrategycues.txt'
                   ]

condition_list = [
                  'arrowblocks',
                  'diststrategycues',
                  'negflowstrategycues',
                  'negmemorywords',
                  'neumemorywords',
                  'reapstrategycues'
                  ]

base_input_dir = os.path.join(this_env['MYDIR'], 'Data/bxh2bids_test_stuff')

base_output_dir = os.path.join(this_env['MYDIR'], 'Data/bxh2bids_test_stuff')

sub_dir = os.path.join('sub-{sub}', 'ses-{ses}', 'func')

tsv_directory = os.path.join(base_output_dir, sub_dir.format(sub=sub, ses=session))
print('Calling fsl2tsv for subject: {}'.format(sub))

file_list = []
for element in input_file_list:
    file_list.append(os.path.join(base_input_dir, element))

ftt.fsl2tsv(sub, session, task, run, tsv_directory, file_list, condition_list)

print('Done!')
