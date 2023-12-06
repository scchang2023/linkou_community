import numpy as np

data=np.genfromtxt("pig.csv",delimiter=",",skip_header=1)
print(f"市場全年成交最高平均重量{data[:,1].max()}")
print(f"市場全年成交最低平均價{data[:,2].min()}")
print(f"市場全年總成交頭數{data[:,0].sum()}")
total_sales=(data[:,0]*data[:,1]*data[:,2])
print(f"市場全年總成交金額{total_sales.sum()}")
print(f"市場全年成交平均每頭金額{total_sales.sum()/data[:,0].sum()}")
