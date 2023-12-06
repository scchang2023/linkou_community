import pandas as pd

df=pd.read_csv("宜蘭縣旅館名冊.csv",encoding="utf-8", sep=",")
df=df.iloc[:,[3,9]]
print(df)
df.to_csv("宜蘭縣旅館名冊1.csv")
df.to_csv("宜蘭縣旅館名冊2.csv",index=False)