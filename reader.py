import csv




def read_csv_files(files):
    rows = []

    for file_path in files:
        with open(file_path, newline='', encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                rows.append(row)

    return rows