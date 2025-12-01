import csv

with open("manualdata.csv","r") as rcsv:
    csv_reader = csv.reader(rcsv)
    print(csv_reader)

    fields = next(csv_reader)
    print(fields)
    for line in csv_reader:
        print(line)