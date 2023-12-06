import pandas as pd

dfs=pd.read_html("https://rate.bot.com.tw/xrt?Lang=zh-TW")
df=dfs[0]
df=df.iloc[:,0:3]
df.columns=["幣別","本行買入","本行賣出"]
df["幣別"]=df["幣別"].str.split(" ").str[0]
print(df)
df.to_excel("currency.xlsx")
