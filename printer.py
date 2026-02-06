from tabulate import tabulate


def print_report(data):
    headers = ["Country", "AVG GDP"]
    print (tabulate(data, headers=headers))