
import fsl_tsv_tools as ftt
import os

this_env = os.environ

sub_list = [
            'EM0038'
            ]

session = 'day3'
task = 'emoreg'
run = '03'

input_file_list = [
                   'EM0038_run3_arrowblocks_fslconds.txt',
                   'EM0038_run3_diststrategycues_fslconds.txt',
                   'EM0038_run3_negflowstrategycues_fslconds.txt',
                   'EM0038_run3_negmemorywords_fslconds.txt',
                   'EM0038_run3_neumemorywords_fslconds.txt',
                   'EM0038_run3_reapstrategycues_fslconds.txt'
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

for subjID in sub_list:
    tsv_directory = os.path.join(base_output_dir, sub_dir.format(sub=subjID, ses=session))
    print('Calling fsl2tsv for subject: {}'.format(subjID))

    file_list = []
    for element in input_file_list:
        file_list.append(os.path.join(base_input_dir, element))

    ftt.fsl2tsv(subjID, session, task, run, tsv_directory, file_list, condition_list)

print('Done!')
