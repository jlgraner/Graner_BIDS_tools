import fsl_tsv_tools as ftt
import os

this_env = os.environ

input_file = '[[YOUR_INPUT_TSV_FILE]]'

output_dir = '[[YOUR_OUTPUT_DIRECTORY]]'

ftt.tsv2fsl(input_file, output_dir)

print('Done!')