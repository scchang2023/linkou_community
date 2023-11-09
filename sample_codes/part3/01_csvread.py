import csv

with open("csvfile.csv", newline="", encoding="utf-8") as csvfile:
    rows=csv.reader(csvfile)
    for row in rows:
        print(row)