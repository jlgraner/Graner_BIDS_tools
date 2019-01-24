
import fsl_tsv_tools as ftt
import os

this_env = os.environ

sub = '[[SUBJECT ID]]'
ses = '[[SESSION ID]]'
task = '[[TASK NAME]]'
run = '[[RUN NUMBER]]'

input_file_list = [
                   '[[FSL TXT FILE 1]]',
                   '[[FSL TXT FILE 2]]',
                   '[[FSL TXT FILE 3]]',
                   '[[FSL TXT FILE 4]]',
                   '[[FSL TXT FILE 5]]',
                   '[[FSL TXT FILE 6]]'
                   ]

condition_list = [
                  '[[FSL CONDITION NAME 1]]',
                  '[[FSL CONDITION NAME 2]]',
                  '[[FSL CONDITION NAME 3]]',
                  '[[FSL CONDITION NAME 4]]',
                  '[[FSL CONDITION NAME 5]]',
                  '[[FSL CONDITION NAME 6]]'
                  ]

input_dir = '[[DIRECTORY CONTAINING THE FILES IN input_file_list]]'

output_dir = '[[DIRECTORY WHERE YOU WANT THE TSV FILE TO BE WRITTEN]]'



print('Calling fsl2tsv for subject: {}'.format(sub))

file_list = []
for element in input_file_list:
    file_list.append(os.path.join(input_dir, element))

ftt.fsl2tsv(sub, ses, task, run, output_dir, file_list, condition_list)

print('Done!')
