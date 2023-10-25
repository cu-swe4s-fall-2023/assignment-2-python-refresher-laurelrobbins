import my_utils
import argparse
import sys

sys.path.insert(0, '../../src')  # noqa


def main():
    args = my_utils.get_args()
    try:
        file_name = args.file_name
    except AttributeError:
        print("possibly wrong variable type. Check argument formatting")
    try:
        result_columm = args.result_column
    except AttributeError:
        print('invalid entry for result_column')
    f = my_utils.file_errors(args.file_name)
    fires = my_utils.get_column(args.file_name,
                                args.query_column,
                                args.query_value,
                                args.result_column)

    operation = args.operation

    if operation == 'mean':
        result = my_utils.mean(my_utils.string_list_convert(fires))
    elif operation == 'median':
        result = my_utils.median(my_utils.string_list_convert(fires))
    elif operation == 'std dev':
        result = my_utils.std_dev(my_utils.string_list_convert(fires))
    else:
        result = my_utils.string_list_convert(fires)

    for item in result:
        print(item)


if __name__ == "__main__":
    main()
