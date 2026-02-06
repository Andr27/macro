import argparse 

from reader import read_csv_files
from reports.init import get_report 
from printer import print_report



def parse_args():
    parser = argparse.ArgumentParser(description='Macroeconomic report')
    parser.add_argument(
        "--files",
        nargs="+",
        required=True,
        help="Paths to csv files",
    )
    parser.add_argument(
        '--report',
        required=True,
        help='Report name (e.g. average-gdp)',
    )
    return parser.parse_args()


def main():
    args = parse_args()

    rows = read_csv_files(args.files)
    report = get_report(args.report)
    result = report.build(rows)
    print_report(result)



if __name__ == '__main__':
    main()