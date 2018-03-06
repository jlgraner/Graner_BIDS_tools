import fsl_tsv_tools as ftt
import os



input_file = '/mnt/keoki/experiments2/Graner/Data/bxh2bids_test_stuff/sub-EM0038/ses-day3/func/sub-EM0038_ses-day3_task-emoreg_run-03_events.tsv'

output_dir = '/mnt/keoki/experiments2/Graner/Data/bxh2bids_test_stuff/sub-EM0038/ses-day3/func/'

ftt.tsv2fsl(input_file, output_dir)

print('Done!')