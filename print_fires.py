import my_utils
import argparse
import sys 

sys.path.insert(0, '../../src')  # noqa


def main():
    args = my_utils.get_args()
    f = my_utils.file_errors(args.file_name)
    fires = my_utils.get_column(args.file_name,
                                args.query_column,
                                args.query_value,
                                args.result_column)
    print(fires)


if __name__ == "__main__":
    main()

