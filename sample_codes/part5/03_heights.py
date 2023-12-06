import numpy as np

data=np.genfromtxt("heights.csv",delimiter=",",skip_header=1)
heights=np.array(data[:,2])
print(heights)
print(f"Mean height:{heights.mean()}")
print(f"Standard deviation:{heights.std()}")
print(f"Minimum height:{heights.min()}")
print(f"Maximum height:{heights.max()}")
print(f"25th percentile:{np.percentile(heights,25)}")
print(f"Median:{np.median(heights)}")
print(f"75th percentile:{np.percentile(heights,75)}")
