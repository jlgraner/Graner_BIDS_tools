
import os
import pandas as pd


def read_confound_file(input_file):

    if not os.path.exists(input_file):
        raise RuntimeError('Input file cannot be found {}'.format(input_file))

    #Read in the confound file as a pandas dataframe
    with open(input_file, 'r') as fid:
        data = pd.read_csv(input_file, sep='\t', engine='python')

    return data



def remove_rows(dataframe, rows_to_exclude):
    new_dataframe = dataframe.drop(range(rows_to_exclude))

    return new_dataframe


def add_columns(source_dataframe, target_dataframe, column_list):
    # new_data = pd.DataFrame()
    for element in column_list:
        if element not in source_dataframe.keys():
            raise RuntimeError('Column name not found in source dataframe header: {}'.format(element))
        else:
            target_dataframe[element] = source_dataframe[element]

    return target_dataframe


def exclude_columns(dataframe, column_list):
    new_data = dataframe
    for element in column_list:
        if element not in dataframe.keys():
            raise RuntimeError('Column name not found in header: {}'.format(element))
        else:
            new_data.drop(element, axis=1)

    return new_data

def match_columns(dataframe, column_label):
    name_list = dataframe.keys()
    match_list = []
    for element in name_list:
        if column_label in element:
            match_list.append(element)

    return match_list