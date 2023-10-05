test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

#run <test name> <program> <argument 1> <argument 2> <...>

run query_search python src/print_fires.py --file_name 'src/test_file.csv' --query_column 0 --query_value 'Afghanistan' --result_column 2  
assert_exit_code 0

run bad_query_search python print_fires.py --file_name 'src/nonexistent_file.csv' --query_column 0 --query_value 'Afghanistan' --result_column 2
assert_exit_code 2

run mean python src/print_fires.py --file_name 'src/test_file.csv' --query_column 0 --query_value 'Afghanistan' --result_column 2 --operation 'mean'
assert_exit_code 0

run median python src/print_fires.py --file_name 'src/test_file.csv' --query_column 0 --query_value 'Afghanistan' --result_column 2 --operation 'median'
assert_exit_code 0

run std_dev python src/print_fires.py --file_name 'src/test_file.csv' --query_column 0 --query_value 'Afghanistan' --result_column 2 --operation 'std dev'
assert_exit_code 0
