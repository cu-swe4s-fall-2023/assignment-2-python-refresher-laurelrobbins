import csv

def get_column(file_name, query_column, query_value, result_column):
    array = [] #empty list for data to go in
    with open(file_name, newline='') as simpler:
        csv_reader = csv.reader(simpler)
        for row in csv_reader: #loops through each line and adds data to list when condition is met
            if row[query_column] == query_value:
                array.append(row[result_column])
    return array

