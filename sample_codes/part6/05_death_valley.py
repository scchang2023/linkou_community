import csv
from datetime import datetime
from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']  
plt.rcParams['axes.unicode_minus']=False

with open("death_valley.csv") as f:
    reader=csv.reader(f)
    header_row=next(reader)
    dates,highs,lows=[],[],[]
    for row in reader:
        try:
            current_date=datetime.strptime(row[0], "%Y-%m-%d")
            high=(int(row[1])-32)*5/9
            low=(int(row[3])-32)*5/9
        except ValueError:
            print(current_date,"missing data")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
plt.plot(dates,highs,c="red")
plt.plot(dates,lows,c="blue")
plt.title("Daily high and low temperatures")
plt.xlabel("日期")
plt.ylabel("溫度")
plt.show()

# =============================================================================
# 利用pandas
# =============================================================================
# import pandas as pd
# from matplotlib import pyplot as plt

# plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']  
# plt.rcParams['axes.unicode_minus']=False

# df=pd.read_csv("death_valley.csv",encoding="utf-8", sep=",")
# df[df.columns[0]]=pd.to_datetime(df[df.columns[0]])
# df[df.columns[[1,3]]]=(df[df.columns[[1,3]]]-32)*5/9

# plt.plot(df.iloc[:,0],df.iloc[:,1],c="red")
# plt.plot(df.iloc[:,0],df.iloc[:,3],c="blue")
# plt.title("Daily high and low temperatures")
# plt.xlabel("日期")
# plt.ylabel("溫度")
# plt.show()

# =============================================================================
# 動畫
# %matplotlib qt5
# Tools > Preferences > IPython Console > Graphics > Backend and change it from "Inline" to "Automatic"
# =============================================================================
# import pandas as pd
# from matplotlib import pyplot as plt
# from matplotlib import animation

# plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']  
# plt.rcParams['axes.unicode_minus']=False

# df=pd.read_csv("death_valley.csv",encoding="utf-8", sep=",")
# df[df.columns[0]]=pd.to_datetime(df[df.columns[0]])
# df[df.columns[[1,3]]]=(df[df.columns[[1,3]]]-32)*5/9

# fig=plt.figure()
# def run(i=int):
#     plt.plot(df[:i].iloc[:,0],df[:i].iloc[:,1],c="red")
#     plt.plot(df[:i].iloc[:,0],df[:i].iloc[:,3],c="blue")
#     plt.title("Daily high and low temperatures")
#     plt.xlabel("日期")
#     plt.ylabel("溫度")
# animator=animation.FuncAnimation(fig,run,interval=10,cache_frame_data=False)
# plt.show()