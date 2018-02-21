
import os
import pandas as pd


def read_confound_file(input_file):
    ##############################
    # PURPOSE: Make sure a file is there, then read it in as a pandas Data Frame
    # INPUTS:
    #          input_file: a string containing the full path and file name of
    #                      the input confound file to read
    # RETURN:
    #          data: a pandas data frame containing the contents of the input_file
    ###############################
    if not os.path.exists(input_file):
        raise RuntimeError('Input file cannot be found {}'.format(input_file))
    #Read in the confound file as a pandas dataframe
    with open(input_file, 'r') as fid:
        data = pd.read_csv(input_file, sep='\t', engine='python')
    return data

def add_columns(source_dataframe, target_dataframe, column_list):
    ##############################
    # PURPOSE: Add columns from one data frame to another data frame
    # INPUTS:
    #          source_dataframe: a pandas data frame containing the columns
    #                            you want to copy into the other one.
    #          target_dataframe: a pandas data frame to which you want to add
    #                            data columns
    #          column_list: list of strings containing the names of columns to
    #                       be copied from the source into the target
    # RETURN:
    #          target_dataframe
    ###############################
    for element in column_list:
        if element not in source_dataframe.keys():
            raise RuntimeError('Column name not found in source dataframe header: {}'.format(element))
        else:
            target_dataframe[element] = source_dataframe[element]
    return target_dataframe

def exclude_columns(dataframe, column_list):
    ##############################
    # PURPOSE: Remove specific data columns from a data frame
    # INPUTS:
    #          dataframe: a pandas data frame containing the columns
    #                     you want to remove.
    #          column_list: list of strings containing the names of columns to
    #                       be removed
    # RETURN:
    #          new_data: version of dataframe with the desired columns removed
    ###############################
    new_data = dataframe
    for element in column_list:
        if element not in dataframe.keys():
            raise RuntimeError('Column name not found in header: {}'.format(element))
        else:
            new_data.drop(element, axis=1)
    return new_data

def match_columns(dataframe, column_label):
    ##############################
    # PURPOSE: Create a list of data column names that contain the input string
    # INPUTS:
    #          dataframe: a pandas data frame from which you want to get data
    #                     column names that match the passed label.
    #          column_label: keep all data columns containing this string in
    #                        their names
    # RETURN:
    #          match_list: a list of data frame column names as strings
    ###############################
    name_list = dataframe.keys()
    match_list = []
    for element in name_list:
        if column_label in element:
            match_list.append(element)
    return match_list