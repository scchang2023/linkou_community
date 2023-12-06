import pandas as pd

df=pd.read_excel("雲林縣統計年報-家庭收支類.xls")
df=df.iloc[:,[1,2]]
print(df)
df.to_excel("雲林縣統計年報-家庭收支類1.xls")
df.to_excel("雲林縣統計年報-家庭收支類2.xls",index=False)

# pip install xlwt
# pip install xlrd