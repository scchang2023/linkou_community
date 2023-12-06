import pandas as pd
import json

with open("路邊停車資訊.json",encoding="utf-8") as file:
    data=json.load(file) 
df=pd.DataFrame(data["roadsides"])
df=df.iloc[:,[0,3,4]]
print(df)
df.to_csv("路邊停車資訊1.csv",index=False)
df.to_json("路邊停車資訊1.json")
df.to_json("路邊停車資訊2.json",force_ascii=False)