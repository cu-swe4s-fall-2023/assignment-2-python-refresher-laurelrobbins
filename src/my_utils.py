import argparse
import csv
import sys
import statistics


def get_args():
    parser = argparse.ArgumentParser(
        description='pull specified data from csv file',
        prog='my_utils')
    parser.add_argument('--file_name',
                        type=str,
                        help='name of the file',
                        required=True)
    parser.add_argument('--query_column',
                        type=int,
                        help='name of the column you want to pull from',
                        required=True)
    parser.add_argument('--query_value',
                        type=str,
                        help='value you want to pull data for',
                        required=True)
    parser.add_argument('--result_column',
                        type=int,
                        help='data from the value you selected',
                        required=False)
    parser.add_argument('--operation',
                        type=str,
                        choices=['mean', 'median', 'std dev'],
                        help='Calculate mean, median, or std dev of values',
                        required=False)

    args = parser.parse_args()
    return args


def file_errors(file_name):
    f = None
    try:
        f = open(file_name, 'r')
    except FileNotFoundError:
        sys.exit('Not able to find ' + file_name)
    except PermissionError:
        sys.exit('Unable to open' + file_name + '. Check permissions of file')
    return f


def get_column(file_name,
               query_column,
               query_value,
               result_column=1):
    """ pulls specified data from csv file and returns it in a list

    Parameters
    ----------
    file_name : the name of the csv file with the data you want to pull from
    query_column : the column (indexed at 0) you want to pull from
    query_value : the specific value you want to pull data for
    result_column : the data from the value you selected

    Returns
    -------
    array : list of result_column
    """
    array = []
    # empty list for data to go in
    with open(file_name, newline='') as simpler:
        csv_reader = csv.reader(simpler)
        for row in csv_reader:
            # loops through lines and adds data to list when condition is met
            try:
                if row[query_column] == query_value:
                    array.append(row[result_column])
            except IndexError:
                sys.exit('Column does not exist. Check result_column input.')
    return array


def mean(array):
    mean = sum(array)/len(array)

    return mean


def median(array):
    array.sort()
    # if odd number of values
    if len(array) == 0:
        median = None
    elif len(array) % 2 == 1:
        median = array[((len(array)) // 2)]
    # if even number of values
    elif len(array) % 2 != 1:
        medleft = array[((len(array)-1) // 2)]
        medright = array[((len(array)) // 2)]
        median = (medleft+medright) / 2
    else:
        median = "check formatting for list of input values"

    return median


# I asked ChatGGPT how to find std dev of a sample without importing a library
def std_dev(array):
    if len(array) == 0:
        std_dev = None
    elif len(array) > 0:
        mean = sum(array) / len(array)
        squared_diff = [(x - mean) ** 2 for x in array]
        variance = sum(squared_diff) / (len(array)-1)
        std_dev = variance ** 0.5
    else:
        std_dev = "check formatting for list of input values"

    return std_dev


def string_list_convert(array):
    return list(map(float, array))
