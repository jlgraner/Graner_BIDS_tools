
import fsl_tsv_tools as ftt
import os

this_env = os.environ

sub = '[[SUBJECT ID]]' # The ID number you use for this study participant (e.g. 'MS001')
ses = '[[SESSION ID]]' # A short identifier for this scan session (e.g. 'day1')
task = '[[TASK NAME]]' # The short name of your fMRI task (e.g. 'stroop')
run = '[[RUN NUMBER]]' # Two-digit Run number of the task within the scan session (e.g. '01')

input_file_list = [
                   '[[FSL TXT FILE 1]]', #List of .txt files containing the FSL-formatted event information for task conditions (EVs)
                   '[[FSL TXT FILE 2]]', # (e.g. 'MS001_day1_stroop_01_incongruent.txt')
                   '[[FSL TXT FILE 3]]', # The number of .txt files in this list must match the number of conditions in the
                   '[[FSL TXT FILE 4]]', # condition list below. The order of the .txt files must also correspond to the
                   '[[FSL TXT FILE 5]]', # order of the conditions. All of these files must be in the same directory.
                   '[[FSL TXT FILE 6]]'
                   ]

condition_list = [
                  '[[FSL CONDITION NAME 1]]', #List of short names of task conditions to be used in the output .tsv file
                  '[[FSL CONDITION NAME 2]]', # (e.g. 'incongruent')
                  '[[FSL CONDITION NAME 3]]', # The number of conditions in this list must match the number of .txt files
                  '[[FSL CONDITION NAME 4]]', # in the file list above. The order of the conditions must also correspond to
                  '[[FSL CONDITION NAME 5]]', # the order of the text files.
                  '[[FSL CONDITION NAME 6]]'
                  ]

input_dir = '[[DIRECTORY CONTAINING THE FILES IN input_file_list]]' # (e.g. '/usr/home/data/mystudy/MS001/fsl_ev_files/')

output_dir = '[[DIRECTORY WHERE YOU WANT THE TSV FILE TO BE WRITTEN]]' # (e.g. '/usr/home/data/mystudy/MS001/BIDS_tsv_file/'; MUST EXIST BEFORE RUNNING)


#-----------Do not edit below this line------------
print('Calling fsl2tsv for subject: {}'.format(sub))

file_list = []
for element in input_file_list:
    file_list.append(os.path.join(input_dir, element))

ftt.fsl2tsv(sub, ses, task, run, output_dir, file_list, condition_list)

print('Done!')
