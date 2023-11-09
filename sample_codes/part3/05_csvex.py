import csv

with open("宜蘭縣旅館名冊.csv", newline="", encoding="utf-8") as csvfile:
    rows = csv.DictReader(csvfile)
    for row in rows:
        for field in rows.fieldnames:
            print(row[field],end=" ")
        print("")  

# with open("宜蘭縣旅館名冊.csv", newline="", encoding="utf-8") as csvfile:
#     rows = csv.DictReader(csvfile)
#     for row in rows:
#         print(row["中文名稱"], row["登記地址"])
    
# with open("宜蘭縣旅館名冊.csv", newline="", encoding="utf-8") as csvfile:
#     rows = csv.DictReader(csvfile)
#     for row in rows:
#         print(row[rows.fieldnames[3]], row[rows.fieldnames[9]])
 