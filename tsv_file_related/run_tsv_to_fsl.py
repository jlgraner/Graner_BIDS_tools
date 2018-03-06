import fsl_tsv_tools as ftt
import os

# fsl2tsv(subjID, session, task, run, TSV_directory, file_list, condition_list)

# sub_list = [
#             'EM0038'
#             ]

# session = 'day3'
# task = 'emoreg'
# run = '03'

# input_file_list = [
#                    'EM0038_run3_arrowblocks_fslconds.txt',
#                    'EM0038_run3_diststrategycues_fslconds.txt',
#                    'EM0038_run3_negflowstrategycues_fslconds.txt',
#                    'EM0038_run3_negmemorywords_fslconds.txt',
#                    'EM0038_run3_neumemorywords_fslconds.txt',
#                    'EM0038_run3_reapstrategycues_fslconds.txt'
#                    ]

# condition_list = [
#                   'arrowblocks',
#                   'diststrategycues',
#                   'negflowstrategycues',
#                   'negmemorywords',
#                   'neumemorywords',
#                   'reapstrategycues'
#                   ]

input_file = '/mnt/keoki/experiments2/Graner/Data/bxh2bids_test_stuff/sub-EM0038/ses-day3/func/sub-EM0038_ses-day3_task-emoreg_run-03_events.tsv'

output_dir = '/mnt/keoki/experiments2/Graner/Data/bxh2bids_test_stuff/sub-EM0038/ses-day3/func/'

ftt.tsv2fsl(input_file, output_dir)

print('Done!')