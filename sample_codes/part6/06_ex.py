import matplotlib.pyplot as plt
import csv

plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']  
plt.rcParams['axes.unicode_minus']=False

x=[]
y=[]
with open("banana.csv","r",encoding="utf-8") as csvfile:
    plots=csv.reader(csvfile,delimiter=",")
    for row in plots:
        x.append(row[0])
        y.append(float(row[1]))
plt.plot(x,y,label="香蕉")
plt.xlabel("成交日期")
plt.ylabel("成交平均價")
plt.ylim([15,25])
plt.title("香蕉成交行情")
plt.legend()
plt.show()