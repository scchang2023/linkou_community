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

與NumPy陣列一樣，相關索引可以透過熟悉的Python方括號表示法訪問資料

```python
print(data[1])
print(data[1:3])
```

```python
0.5
1    0.50
2    0.75
dtype: float64
```

---

### Series 可被看一般化的NumPy 陣列

- Series物件可以與一維NumPy陣列互換，其區別在於索引的存在。
- Numpy陣列有一個隱式定義的整數索引用於訪問值。
- Pandas Series有一個顯式定義的索引與值相關聯。這個顯式索引定義為Series物件提供了額外的功能。 例如，索引不必是整數，但可以包含任何所需類型的值。甚至如果我們願意，我們可以使用字符串作為索引。

```python
import pandas as pd

data=pd.Series([0.25,0.5,0.75,1.0], index=["a","b","c","d"])
print(data)
print(data["b"])
```

```python
a    0.25
b    0.50
c    0.75
d    1.00
dtype: float64
0.5
```

---

甚至可以使用非連續或無順序的索引：

```python
data=pd.Series([0.25,0.5,0.75,1.0], index=[2,5,3,7])
print(data)
print(data[5])
```

```python
2    0.25
5    0.50
3    0.75
7    1.00
dtype: float64
0.5
```

---

### Series 可以當作特殊的字典

- 字典是將任意鍵映射到一組任意值的結構，而Series是將鍵入的鍵映射到一組鍵入值的結構。
- 這種類型很重要：正如NumPy陣列後面的特定於類型的編譯代碼使其比某些操作的Python串列更有效，Series的類型訊息使得它比Python字典更有效操作。

```python
population_dict={"California":39250017,
                 "Texas":27862596,
                 "Florida":20612439,
                 "New York":19745289,
                 "Illinois":12801539}
population=pd.Series(population_dict)
print(population)
```

```python
California    39250017
Texas         27862596
Florida       20612439
New York      19745289
Illinois      12801539
dtype: int64
```

---

- 預設情況下，將創建一個Series，其中索引是從排序鍵中提取的。從這裡，可以執行典型的字典式項目訪問：

```python
print(population["California"]) # 39250017
```

- 但是與字典不同，Series也支援陣列樣式的操作，例如切片：

```python
print(population["California":"Illinois"])
```

```python
California    39250017
Texas         27862596
Florida       20612439
New York      19745289
Illinois      12801539
dtype: int64
```

---

### Pandas DataFrame物件

Pandas的DataFrame被認為是NumPy陣列的一般化，也可以被認為是Python字典的特化。

---

### DataFrame作為一般化的NumPy陣列

- DataFrame是具有靈活列索引和靈活行名的二維陣列的模擬，可以將"DataFrame"視為一系列對齊的Series物件。
- 在這裡，"對齊"是指它們共享相同的索引。下面首先構建一個新的Series，列出上一節討論的五個州中每個州的區域：

```python
California    423967
Florida       170312
Illinois      149995
New York      141297
Texas         695662
dtype: int64
```

---

現在我們已經將它與之前的population Series一起使用，我們可以使用字典來建構包含這些訊息的單個二維物件：

```python
states=pd.DataFrame({"population":population,"area":area})
print(states)
```

```python
population    area
California    39250017  423967
Florida       20612439  170312
Illinois      12801539  149995
New York      19745289  141297
Texas         27862596  695662
```

---

DataFrame有一個index屬性，可以訪問索引標籤，還有一個columns屬性，它是一個包含行標籤的Index物件：

```python
print(states.index)
print(states.columns)
```

```python
Index(['California', 'Florida', 'Illinois', 'New York', 'Texas'], dtype='object')
Index(['area', 'population'], dtype='object')
```

因此，DataFrame可以被認為是二維NumPy陣列的一般化，其中行和列都具有用於訪問資料的通用索引。

---

### Series中資料的選取

- Series物件可用於一維NumPy陣列與標準的Python字典。
- 像字典一樣，Series物件提供從一組鍵到一組值的映射。

```python
data=pd.Series([0.25,0.5,0.75,1.0],
               index=["a","b","c","d"])
print(data)
print(data["b"])
```

```python
a    0.25
b    0.50
c    0.75
d    1.00
dtype: float64
0.5
```

---

Series物件甚至可以用類似字典的語法修改。如同透過分配新鍵來擴展字典一樣，可以透過分配新的索引值來擴展Series：

```python
data["e"]=1.25
print(data)
```

```python
a    0.25
b    0.50
c    0.75
d    1.00
e    1.25
dtype: float64
```

---

### 將Series當作一維陣列

一個Series建立在這個類似字典的界面上，並透過與NumPy陣列相同的基本機制提供陣列樣式的項目選擇 - 即 slices、masking 和 fancy indexing 。這些例子如下：

```python
print(data["a":"c"])
print(data[0:2])
```

```python
a    0.25
b    0.50
c    0.75
dtype: float64
a    0.25
b    0.50
dtype: float64
```

---

其中切片可能是混亂的根源。請留意，當使用顯式索引進行切片時（即data ["a":"c"]），最終索引在切片中包含，而在使用隱式索引進行切片時（即data [0:2]），最終索引從切片中排除。

```python
data["e"]=1.25
print(data[(data>0.3) & (data<0.8)])
print(data[["a","e"]])
```

```python
b    0.50
c    0.75
dtype: float64
a    0.25
e    1.25
dtype: float64
```

---

### 索引採用指令: loc, iloc

這些切片和索引約定可能會引起混淆。例如，如果你的Series有一個顯式的整數索引，那麼索引操作如data[1]將使用顯式索引，而切片操作如data[1:3]將使用隱式的Python風格索引。

```python
data=pd.Series(["a","b","c"],index=[1,3,5])
print(data)
print(data[1])
print(data[1:3])
```

```python
1    a
3    b
5    c
dtype: object
a
3    b
5    c
dtype: object
```

---

- 由於在整數索引的情況下存在這種潛在的混淆，Pandas提供了一些特殊的 indexer 屬性，這些屬性明確地顯示了某些索引方案。
- 這些不是函數方法，而是將特定切片接口顯示給Series中的資料的屬性。
- 首先，loc屬性允許索引和切片始終引用顯式索引：

```python
print(data.loc[1])
print(data.loc[1:3])
```

```python
a
1    a
3    b
dtype: object
```

---

iloc屬性允許索引和切片引用隱式的Python樣式索引

```python
print(data.iloc[1])
print(data.iloc[1:3])
```

```python
b
3    b
5    c
dtype: object
```

---

### DataFrame中的資料選取

- DataFrame類似二維或結構化陣列與共享相同索引的Series結構字典。
- 將DataFrame作為相關Series物件的字典。以美國各州面積與人口數的來舉例。

```python
area=pd.Series({"California":423967,"Texas":695662,
                "New York":141297,"Florida":170312,
                "Illinois":149995})
pop=pd.Series({"California":39250017,"Texas":27862596,
               "Florida":20612439,"New York":19745289,
               "Illinois":12801539})
data=pd.DataFrame({"area":area,"pop":pop})
print(data)
```

```python
 area       pop
California  423967  39250017
Florida     170312  20612439
Illinois    149995  12801539
New York    141297  19745289
Texas       695662  27862596
```

---

構成DataFrame行的單個Series可以透過column名稱的字典式索引來訪問

```python
print(data["area"])
```

```python
California    423967
Florida       170312
Illinois      149995
New York      141297
Texas         695662
Name: area, dtype: int64
```

---

這種字典式語法也可用於修改物件，在這種情況下添加一個新行：

```python
data["density"]=data["pop"]/data["area"]
print(data)
```

```python
              area       pop     density
California  423967  39250017   92.578000
Florida     170312  20612439  121.027520
Illinois    149995  12801539   85.346438
New York    141297  19745289  139.743158
Texas       695662  27862596   40.051916
```

---

Pandas再次使用前面提到的loc、iloc索引器。使用iloc索引器，我們可以將底層陣列索引為好像它是一個簡單的NumPy陣列（使用隱式的Python樣式索引），但結果中保留了DataFrame索引和行標籤：

```python
print(data.iloc[:3,:2])
```

```python
area       pop
California  423967  39250017
Florida     170312  20612439
Illinois    149995  12801539
```

---

類似地，使用loc索引器，我們可以使用顯式索引和行名稱以類似陣列的樣式索引基礎資料：

```python
print(data.loc[:"Illinois",:"pop"])
```

```python
              area       pop
California  423967  39250017
Florida     170312  20612439
Illinois    149995  12801539
```

---

### Pandas的應用

- pandas.read_csv
- pandas.DataFrame.to_csv
- pandas.read_json
- pandas.DataFrame.to_json
- pandas.read_xml
- pandas.DataFrame.to_xml
- pandas.read_excel
- pandas.DataFrame.to_excel
- pandas.read_html

---

### Pandas讀取csv

利用Pandas將csv內容讀進DataFrame

[04_pandas_csv.py][04_pandas_csv.py]

---

### Pandas讀取json

利用Pandas將json內容讀進DataFrame

[05_pandas_json.py][05_pandas_json.py]

---

[04_pandas_csv.py]: /sample_codes/part5/04_pandas_csv.py
[05_pandas_json.py]: /sample_codes/part5/05_pandas_json.py
