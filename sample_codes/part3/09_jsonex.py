import json

with open("路邊停車資訊.json",encoding="utf-8") as file:
    data=json.load(file) 
    for item in data["roadsides"]:
        print(item["rd_name"],item["rd_count"],item["use_cnt"])
        