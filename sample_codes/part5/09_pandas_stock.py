import pandas as pd

dfs=pd.read_html("http://www.stockq.org/market/asia.php")
df=dfs[9]
df.columns=df.iloc[1]
df.drop([0,1],inplace=True)
df=df.reset_index(drop=True)
print(df)
df.to_excel("stock.xlsx")
