import my_utils
#query_column = country_column
#query_value = country
#result_column = fires_column 

#if country_column = country, add it to array. This is how we pick specific fields from the data set. 
#country 
query_value = 'United States of America'
query_column = 0
result_column = 3
file_name = 'Agrofood_co2_emission.csv'

fires = my_utils.get_column(file_name, query_column, query_value, result_column)

print(fires)

