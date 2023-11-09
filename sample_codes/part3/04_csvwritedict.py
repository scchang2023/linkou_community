import csv

with open("csvfile.csv", "w", newline="", encoding="utf-8") as csvfile:
    fieldnames=["姓名", "身高", "體重"]
    writer=csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({"姓名": "趙一哥", "身高": 175, "體重": 60})
    writer.writerow({"姓名": "錢二姊", "身高": 165, "體重": 57})