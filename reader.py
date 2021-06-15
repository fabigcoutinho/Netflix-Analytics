import csv

input_file = csv.DictReader(open("data/views.csv"))

for row in input_file:
    print(row['Title'])