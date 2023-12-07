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
