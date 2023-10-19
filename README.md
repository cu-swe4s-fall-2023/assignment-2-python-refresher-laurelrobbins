[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/oQi7O4AA)

# Report for Assignment 7
Introduction: 
This report includes data for wildfires in three countries, Brazil, Canada, and Mexico. Evaluating fires is an important part of wildlife conservation. 

Results: 

![Brazil](doc/Brazil.png?raw=true "Brazil")
![Canada](doc/Canada.png?raw=true "Canada")
![Mexico](doc/Mexico.png?raw=true "Mexico")

Methods:
To get these results, a snakemake workflow was used which first downloaded data from a public dataset, then pulled out data of interest from the csv file, and finally plotted the data in a histogram format using the matplotlib library.

# my_utils.py 
Purpose: contains a function get_column which uses the four variables file_name, query_column, query_value, result_column to pull specified data from a csv file and put the outputs within a list. 
file_name = the name of the csv file with the data you want to pull from
query_column = the column (indexed at 0) you want to pull from
query_value = the specific value you want to pull data for
result_column = the data from the value you selected

# Example of how to use my_utils
print_fires.py 
To use my_utils, use a main function that calls get_args, file_error, and get_column. 

In a shell script (run.sh), input the three required parameters file_name, query_column, and query_value. Optionally include result_column and an operation (either mean, median, or std dev). 

Output in this example: list containing the number of fires in different years for only the Unites States of America. 

# Continuous Integration
Automatically runs functional tests, unit tests, and PEP8 style checks. 

# Installing software
1.) clone assignment-2-python-refresher-laurelrobbins from github. 

2.) download Agrofood_co2_emission.csv

3.) move Agrofood_co2_emission.csv to src folder

4.) change working directory to follow path of cloned repository and into src folder

5.) in run.sh file, use:

python print_fires.py --file_name 'Agrofood_co2_emission.csv' --query_column <query column of interest> --query_value <query value of interest> --result_column <result column of interest>

example of input: 
python print_fires.py --file_name 'Agrofood_co2_emission.csv' --query_column 0 --query_value 'United States of America' --result_column 3 --operation 'mean'

6.) In the command line, run the shell file using: bash run.sh
    

