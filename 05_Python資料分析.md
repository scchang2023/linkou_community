# Python</br>資料分析

章士祺

[TOC]

---

## 資料分析

- 資料分析是由原始資料轉換的幾個步驟組成的過程，基於收集的資料進行處理，以產生可視化結果，並且可以透過數學模型化來進行預測。
- Python資料分析套件：
  - NumPy套件
  - Pandas套件

---

## NumPy套件

- NumPy是Python語言的一個擴充程式庫，代表 "Numeric Python"
- 是一個由多維陣列物件和用於處理陣列的常式集合組成的程式庫，支援高階大量的維度陣列與矩陣運算。
- 針對陣列運算提供大量的數學函數函式庫，在NumPy上只要能被表示為針對陣列或矩陣運算的演算法，其執行效率幾乎都可以與編譯過的等效C語言程式碼一樣快。

---

### NumPy 建立陣列與存取元素

- NumPy的核心功能是"ndarray"（即n-dimensional array，多維陣列）資料結構。這是一個表示多維度、同質並且固定大小的陣列物件。
- 可以經由傳送串列(list)或元組(tuple)給np.array，即可建立一維陣列。也可以透過np.arange建立一維NumPy Array，np.linspace則可建立一個間隔相同的陣列。
- 一維陣列以索引(Index)存取元素，與Python索引用法相同。

---

- 可以經由直接傳送多維串列(list)給np.array，即可建立多維陣列，接著可以透過np.shape取得其外形(shape)。
- 也可以建立一維陣列，接著利用NumPy的reshape可以轉為所需要的各種外形。
- 多維陣列以二維Index存取元素。

---

### 建立一維NumPy Arrays

可以經由傳送串列(list)或元組(tuple)給np.array即可建立一維陣列。

```python
import numpy as np

a=np.array([1,2,3,4])
b=np.array((1,2,3,4))
print(a)
print(b)
```

```python
[1 2 3 4]
[1 2 3 4]
```

---

也可以透過np.arange建立一維NumPy array。
其使用方式類似Python標準庫中的range。
例如：可在3-30(包含3但不含30)間隔3建立一維陣列。

```python
c=np.arange(3,30,3)
print(c)
```

```python
[ 3 6 9 12 15 18 21 24 27]
```

---

np.linspace 則可建立一個間隔相同的陣列。
例如：可在0-10間建立有5個元素的陣列，間隔相同(均為2.5)

```python
d=np.linspace(0,10,5)
print(d)
```

```python
[ 0.   2.5  5.   7.5 10. ]
```

---

### 一維陣列以索引存取元素

```python
c=np.arange(3,30,3)
print(c)
print(c[0])  # 取得在index位置0的元素
print(c[1])  # 取得在index位置1的元素
print(c[2:6])  # 取得在index位置2-5(包含2但不含6)的子陣列(subarray)
print(c[1:-1:2])  # 取得陣列c中index位置1,3,5,..(各間隔1個元素來選取)的子陣列
```

```python
[ 3  6  9 12 15 18 21 24 27]
3
6
[ 9 12 15 18]
[ 6 12 18 24]
```

---

### 多維陣列

可以經由直接傳送多維串列(list)給np.array即可建立多維陣列。接著可以透過np.shape取得其外形(shape)。例如：two_dim為3*4陣列(3列4行)；three_dim則為2*3*4陣列。

```python
two_dim=np.array([[1,2,3,4],
                  [5,6,7,8],
                  [9,10,11,12]])
three_dim=np.array([[[1,2,3,4],
                     [5,6,7,8],
                     [9,10,11,12]],
                    [[13,14,15,16],
                     [17,18,19,20],
                     [21,22,23,24]]])
print(two_dim.shape)
print(three_dim.shape)
```

```python
(3, 4)
(2, 3, 4)
```

---

也可以建立一維陣列，接著利用numpy的reshape可以轉為所需要的各種外形。例如：a原為1*25陣列，可以reshape為5*5陣列。也可以直接建立陣列後呼叫reshape方法轉為3*4陣列。

```Python
a=np.arange(1,26).reshape(5,5)
print(a.shape)
print(a)
print(a[2,4])
print(np.arange(12).reshape(3,4))
```

```python
(5, 5)
[[ 1  2  3  4  5]
 [ 6  7  8  9 10]
 [11 12 13 14 15]
 [16 17 18 19 20]
 [21 22 23 24 25]]
15
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
```

---

### 多維陣列以索引存取元素

```python
a=np.arange(1,26).reshape(5, 5)
print(a)
print(a[0,1:4])  # 獲取由row 0(第0個橫列)中第1個-第3個元素(不含第4個)產生的一維子陣列
print(a[1:4, 0])  # 獲取由column 0(第0個直行)中第1個-第3個元素(不含第4個)產生的一維子陣列
print(a[::2,::2])  # 獲取一個二維陣列，由橫列與直行中隔個元素產生(0、2、4列與0、2、4行)
print(a[:,1])  # 獲取由整個column 1(第1個直行)中元素產生的一維子陣列

```

```python
[[ 1  2  3  4  5]
 [ 6  7  8  9 10]
 [11 12 13 14 15]
 [16 17 18 19 20]
 [21 22 23 24 25]]
[2 3 4]
[ 6 11 16]
[[ 1  3  5]
 [11 13 15]
 [21 23 25]]
[ 2  7 12 17 22]
```

---

### NumPy聚合(Aggregation)操作

通常在面對大量資料時，要先計算相關資料的摘要統計資訊，NumPy具有內置的聚合操作功能，可用於處理陣列。

---

### 加總、最小值與最大值陣列中的資料值

在NumPy中np.sum語法可以得到陣列的加總值；
np.min與np.max，可用來找尋所給陣列中的最小值與最大值

```python
R=np.random.rand(10)
print(R)
print(np.sum(R))
print(np.min(R),np.max(R))
```

```python
[0.12597012 0.33753979 0.53862893 0.67064193 0.07385547 0.39045373
 0.88689562 0.7726298  0.46136112 0.4216793 ]
4.679655807624898
0.07385547266355796 0.8868956230324035
```

---

### 多維陣列聚合操作

假設有一些儲存在二維陣列中的資料，預設是對整個陣列進行聚合操作，但也可以進行聚合操作是沿行或列聚合。

```python
import numpy as np

M=np.random.random((4,4))
print(M)
print(M.sum())
print(" ==== min ====")
print(M.min(axis=0))
print(M.min(axis=1))
print(" ==== max ====")
print(M.max(axis=0))
print(M.max(axis=1))
print(" ==== sum ====")
print(M.sum(axis=0))
print(M.sum(axis=1))

```

```python
[[0.67432404 0.90712961 0.44047645 0.32877987]
 [0.22445696 0.7424593  0.30067196 0.68027863]
 [0.82869901 0.30264764 0.73512967 0.45221243]
 [0.65522602 0.19209983 0.62297477 0.96143096]]
9.048997139605962
 ==== min ====
[0.22445696 0.19209983 0.30067196 0.32877987]
[0.32877987 0.22445696 0.30264764 0.19209983]
 ==== max ====
[0.82869901 0.90712961 0.73512967 0.96143096]
[0.90712961 0.7424593  0.82869901 0.96143096]
 ==== sum ====
[2.38270603 2.14433638 2.09925285 2.42270188]
[2.35070996 1.94786685 2.31868875 2.43173158]
```

---

### 其他聚合操作

NumPy提供了許多其他聚合函數。 下表提供了NumPy中可用的有用聚合函數的列表：
| 功能名稱          | 說明            |
|---------------|---------------|
| np.sum        | 計算元素之和        |
| np.prod       | 計算元素的乘積       |
| np.mean       | 計算元素的中位數      |
| np.std        | 計算標準差         |
| np.var        | 計算方差          |
| np.min        | 找到最小值         |
| np.max        | 找到最大值         |
| np.argmin     | 查找最小值索引       |
| np.argmax     | 查找最大值索引       |
| np.median     | 計算元素的中位數      |
| np.percentile | 計算元素基於排名的統計數據 |
| np.any        | 評估是否有任何元素為真   |
| np.all        | 評估所有元素是否都為真   |

---

### 範例

[01_agg.py][01_agg.py]
[02_pig.py][02_pig.py]
[03_heights.py][03_heights.py]

[01_agg.py]: /sample_codes/part5/01_agg.py
[02_pig.py]: /sample_codes/part5/02_pig.py
[03_heights.py]: /sample_codes/part5/03_heights.py

---

## Pandas套件：pan(el)-da(ta)-s

- 在最基本的層面上，Pandas套件可以被認為是NumPy結構化陣列的增強版本，其中行和列用標籤而不是簡單的整數索引來標識。
- 由此Pandas在基本資料結構之上提供了許多有用的工具，方法和功能，這三個基本的Pandas資料結構是：Series、DataFrame和Index。
- Series是索引資料的一維陣列；DataFrame是索引資料的二維陣列

---

### Pandas Series 物件

Pandas Series是索引資料的一維陣列，可以從串列或陣列創建，如下所示：

```python
import pandas as pd

data=pd.Series([0.25, 0.5, 0.75, 1.0])
print(data)
```

```python
0    0.25
1    0.50
2    0.75
3    1.00
dtype: float64
```

---

- Series包含了一系列值和一系列索引，我們可以使用values和index屬性來訪問。
- values就只是一個NumPy陣列，index則是類型為pd.Index的類似陣列的物件。

```python
print(data.values)
print(data.index)
```

```python
[0.25 0.5  0.75 1.  ]
RangeIndex(start=0, stop=4, step=1)
```

---
