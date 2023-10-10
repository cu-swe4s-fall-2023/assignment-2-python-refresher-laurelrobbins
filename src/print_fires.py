import my_utils
import argparse
import sys

sys.path.insert(0, '../../src')  # noqa


def main():
    args = my_utils.get_args()
    try:
        file_name = args.file_name
    except AttributeError:
        print("possibly wrong variable type. Check argumant formatting")
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
        result = ('mean: ' +
                  str(my_utils.mean(my_utils.string_list_convert(fires))))
    elif operation == 'median':
        result = ('median: ' +
                  str(my_utils.median(my_utils.string_list_convert(fires))))
    elif operation == 'std dev':
        result = ('std dev of the sample: ' +
                  str(my_utils.std_dev(my_utils.string_list_convert(fires))))
    else:
        result = ('List of values: ' +
                  str((my_utils.string_list_convert(fires))))

    print(result)


if __name__ == "__main__":
    main()
