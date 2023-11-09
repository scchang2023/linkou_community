import csv

with open("csvfile.csv", newline="", encoding="utf-8") as csvfile:
    rows = csv.DictReader(csvfile)
    for row in rows:
        print(row["姓名"], row["身高"], row["體重"])
        # for field in rows.fieldnames:
        #     print(row[field],end=" ")
        # print("")      