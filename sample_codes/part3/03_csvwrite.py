import csv

with open("csvfile.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow(["姓名", "身高", "體重"])
    writer.writerow(["趙一哥", 175, 60])
    writer.writerow(["錢二姊", 165, 57])