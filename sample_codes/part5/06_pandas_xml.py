import pandas as pd

df=pd.read_xml("部落圖書資訊站.xml")
df=df.iloc[:,[2,5,6]]
print(df)
df.to_xml("部落圖書資訊站1.xml")