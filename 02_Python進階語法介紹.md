---
# theme: sky
# width: 1280
# height: 960
# marp: true
---

# Python</br>進階語法介紹

章士祺

[TOC]

---

## 串列的操作

### 串列（List）

串列（又稱為「清單」或「列表」），與其他語言的「陣列（Array）」相同，其功能與變數相類似，是提供儲存資料的記憶體空間。

![02_串列元素配置][02_串列元素配置]

---

### 串列宣告

#### 一維串列宣告

一維串列的宣告方式是將元素置於中括號 ([]) 中，每個元素之間以逗號分隔，語法為：`串列名稱=[元素1,元素2,…]`

例如：宣告 `score` 串列，其元素內容為 `[1, 2, 3, 4, 5]`。

![02_串列元素內容][02_串列元素內容]

---

串列中各個元素資料型態可以相同，也可以不同，例如：

```python
list1=[1, 2, 3, 4, 5]
list2=["香蕉", "蘋果", "橘子"]
list3=[1, "香蕉", True]
```

---

#### 空串列宣告

例如：`list4=[]`

#### 多維串列宣告

例如以下是二維串列範例：

```python
list5=[["joe","1234"], ["mary","3368"], ["david","abcd"]]
print(list5[1])
print(list5[1][1])
```

---

### 讀取串列元素

語法：`串列名稱[索引]`

例如：

```python
list1 = [1, 2, 3, 4]
print(list1[0])
```

---

索引值是從 0 開始計數。索引值不可超出串列的範圍，否則執行時會產生「list index out of range」錯誤。例如：

```python
list4 = ["香蕉", "蘋果", "橘子"]
print(list4[3]) # IndexError: list index out of range
```

索引值可以是負值，表示由串列的最後向前取出， 「-1」表示最後一個元素，「-2」表示倒數第二個元素。同理，負數索引值不可超出串列的範圍，否則執行時會產生錯誤。例如：

```python
list4 = ["香蕉", "蘋果", "橘子"]
print(list4[-4]) # IndexError: list index out of range
```

[01_list1.py][01_list1.py]

---

### 改變串列元素改變串列元素

語法為：串列名稱[索引]=元素內容

例如：

```python
list1=[1, 2, 3, 4, 5]
print(list1[0])
list1[0] = 9
print(list1[0])
```

---

### 使用 for in 讀取串列

語法：

```python
for 變數 in 串列:
    程式區塊
```

例如：

```python
list1 = ["香蕉", "蘋果", "橘子"]
for s in list1:
    print(s)
```

[02_list2.py][02_list2.py]

---

### 使用 for in range 讀取串列

取得串列長度：

迴圈中 range() 函式的範圍通常會利用 len() 函式計算串列的長度。例如：計算 scores 串列的長度，顯示結果為 3。

```python
scores=[83, 98, 56]
print(len(scores)) # 3
```

以 for in range 讀取串列：

```python
scores=[83, 98, 56]
for i in range(len(scores)):
    print(scores[i])
```

[03_list3.py][03_list3.py]

---

### index() 搜尋

語法：`索引值=串列名稱.index(串列元素)`

例如：

```python
list1 = ["香蕉", "蘋果", "橘子"]
n = list1.index("蘋果")
print(n)
m = list1.index("西瓜") # ValueError: '西瓜' is not in list
```

---

### count() 計算次數

語法：`次數=串列名稱. count(串列元素)`

例如：

```python
list1 = ["香蕉", "蘋果", "橘子"]
n = list1.count("蘋果")
m = list1.count("西瓜")
```

---

### 增加串列元素

#### append()方法
  
語法： `串列名稱.append(元素值)`

例如： 在 list1 串列最後面增加一個串列元素「豬頭」。

```python
list1 = [1, 2, 3, 4, 5, 6]
list1.append("豬頭")
print(list1)
```

---

#### insert()方法
  
語法： `串列名稱.insert(索引值,串列元素)`

例如：在 list1 串列索引 3 的位置插入一個串列元素「豬頭」。

```python
list1 = [1, 2, 3, 4, 5, 6]
list1.insert(3, "豬頭")
print(list1)
```

---

如果索引值大於或等於串列元素個數，將如同 append() 方法一樣將串列元素加在最後面。

索引值也可以是負值，表示由串列的最後向前推算，「-1」表示最後一個元素，「-2」表示倒數第二個元素，依此類推。

例如：在 list1 串列索引第 -1、12 的位置插入串列元素。

```python
list1 = [1, 2, 3, 4, 5, 6]
list1.insert(-1, "鳳梨蝦球")
print(list1)
list1.insert(12, "高麗菜")
print(list1)
```

[04_append.py][04_append.py]

---

### 刪除串列元素

#### remvoe()方法

語法：`串列名稱.remove(串列元素)`

例如：刪除 list1 串列中「夏天」的串列元素。

```python
list1 =["春天", "夏天", "秋天", "冬天"]
list1.remove("夏天")
print(list1)
```

---

#### pop()方法

語法：`串列名稱.pop(索引值)`

例如：

```python
list1 = [1, 2, 3, 4, 5, 6]
n = list1.pop()
print(list1, n)
n = list1.pop(2)
print(list1, n)
```

---

#### del 刪除串列元素

刪除串列單一元素語法：`del 串列名稱(n1)`

刪除串列指定範圍元素的語法：`del 串列名稱(n1:n2[:n3])`

例如：

```python
list1 = [1, 2, 3, 4, 5, 6]
del list1[1]
print(list1)
list2 = [1, 2, 3, 4, 5, 6]
del list2[1:5:2]
print(list2)
```

[05_remove.py][05_remove.py]

---

### sort() 由小到大排序

語法：`串列名稱.sort()`

例如：將 list1 串列由小到大排序。

```python
list1 = [3, 2, 1, 5]
list1.sort()
print(list1)
```

---

### reverse() 反轉串列順序

語法：`串列名稱.reverse()`

例如：將 list1 串列順序反轉。

```python
list1 = [3, 2, 1, 5]
list1.reverse()
print(list1)
```

---

### 由大到小排序

語法：

`串列名稱.sort()`

`串列名稱.reverse()`

例如：

```python
list1 = [3, 2, 1, 5]
list1.sort()
print(list1)
list1.reverse()
print(list1)
```

---

### sorted() 排序

語法：`串列名稱2=sorted(串列名稱1, reverse=True)`

例如：將 list1 串列由大到小排序，並儲存在 list2 串列。

```python
list1 = [3, 2, 1, 5]
list2=sorted(list1, reverse=True)
print(list2)
print(list1)
```

[06_sorted.py][06_sorted.py]

---

### 串列常用方法列表

下表串列常用方法：`list1=[1,2,3,4,5,6]`

| 方法                  | 說明          | 範例                 | 結果              |
|---------------------|-------------|--------------------|-----------------|
| list1[n1:n2]        | 取出n1到n2-1元素 | list2=list1[1:4]   | list2=[2,3,4]   |
| list1[n1:n2:n3]     | 同上，取出間隔為n3  | list2=list1[1:4:2] | list2=[2,4]     |
| del list1[n1:n2]    | 刪除n1到n2-1元素 | del list1[1:4]     | list1=[1,5,6]   |
| del list1[n1:n2:n3] | 同上，刪除間隔為n3  | del list1[1:4:2]   | list1=[1,3,5,6] |
| n=len(list1)        | 取得串列元素數目    | n=len(list1)       | n=6             |
| n=min(list1)        | 取得元素最小值     | n=min(list1)       | n=1             |
| n=max(list1)        | 取得元素最大值     | n=max(list1)       | n=6             |
| n=list1.index(n1)   | 第1次n1元素的索引值 | n=list1.index(3)   | n=2             |
| n=list1.count(n1)   | n1元素出現的次數   | n=list1.count(3)   | n=1             |

---

| 方法               | 說明                | 範例                 | 結果                     |
|------------------|-------------------|--------------------|------------------------|
| list1.append(n1) | 將n1元素加在串列最後       | list1.append(8)    | list1=[1,2,3,4,5,6,8]  |
| list1[n1:n2:n3]  | 同上，取出間隔為n3        | list2=list1[1:4:2] | list2=[2,4]            |
| n=list1.pop()    | 取出最後1個元素並由串列中移除元素 | n=list1.pop()      | n=6, list1=[1,2,3,4,5] |
| list1.remove(n1) | 移除第1次的n1元素        | list1.remove(3)    | list1=[1,2,4,5,6]      |
| list1.reverse()  | 反轉串列順序            | list1.reverse()    | list1=[6,5,4,3,2,1]    |
| list1.sort()     | 將串列由小到大排序         | list1.sort()       | list1=[1,2,3,4,5,6]    |

---

## 元組的操作

### 元組（Tuple）

建立元組，使用小括號

語法：`元組名稱=(元素1,元素2, ...)`

例如：

```python
tuple1 = (1, 2, 3, 4, 5)
tuple2 = (1, "紅豆", True)
```

元組的使用方式與串列相同，但不能修改元素值，否則會產生錯誤

```python
tuple3 = ("綠豆", "紅豆", "花生")
tuple3[1]="黃豆" # TypeError: 'tuple' object does not support item assignment
```

---

### 串列和元組互相轉換

Python 提供list命令將元組轉換為串列，tuple命令將串列轉換為元組。

元組轉串列範例：

```python
tuple1=(1,2,3,4,5)
list1=list(tuple1)
list1.append(8)
```

串列轉元組範例：

```python
list2=[1,2,3,4,5]
tuple2=tuple(list2)
tuple2.append(8)
```

---

### 練習題 1

輸入一個整數N，再以迴圈方式輸入N個數字，並將這些數字存入串列中。

輸入一個整數N，將N項的費氏數列存到串列中。

> 所謂費波那契數列，是指在一串數字中，每一項是前兩項的和。數學上的定義為：第 0 項 = 0、第 1 項 = 1、第 n 項 = 第 n-1 項 + 第 n-2 項。從上面的數學定義，我們可以簡單列出數列的 0 到 10 項為：0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55。

---

## 字典的操作

### 建立字典

- 字典的結構，其元素是以「鍵 - 值」對方式儲存，這樣就可使用「鍵」來取得「值」。
- 有多種方式可以建立字典，第一種方式為將元素置於一對大括號「{}」中，其語法為：字典名稱={鍵1:值1,鍵2:值2,…}
- 字串、整數、浮點數等皆可做為「鍵」，但以字串做為「鍵」的情況最多。

---

### 字典取值

字典，與串列最大的不同在於串列元素在記憶體中是依序排列，而字典元素則是隨意放置，沒有一定順序。
![02_字典元素配置][02_字典元素配置]

基本取值方式

語法為：`字典名稱[鍵]`

---

### 當字典的鍵重複時

字典是使用「鍵」做為索引來取得「值」，所以「鍵」必須是唯一，而「值」可以重覆。

如果「鍵」重覆的話，則前面的「鍵」會被覆蓋，只有最後的「鍵」有效，例如：

```python
dict2={"香蕉":20, "蘋果":50, "橘子":30, "香蕉":25}
print(dict2)
```

---

### 當字典的鍵不存在時

若輸入的「鍵」不存在會產生錯誤，因此 Python 另外提供了 get 方法可以取得字典元素值，即使「鍵」不存在也不會產生錯誤，語法為：`字典名稱.get(鍵[預設值])`

| 預設值狀況   | 鍵是否存在        | 返回值                |
|---------|--------------|--------------------|
| 沒有傳入預設值 | 鍵存在</br>鍵不存在 | 返回鍵對應的值</br>返回None |
| 有傳入預設值  | 鍵存在</br>鍵不存在 | 返回鍵對應的值</br>返回預設值  |

[07_dictget.py][07_dictget.py]

### 修改字典

修改字典元素值與在字典中新增元素的語法相同。

語法為：`字典名稱[鍵]=值`

如果「鍵」存在就是修改元素值，新元素值會取代舊元素值，如果「鍵」不存在就是新增元素。

---

### 刪除字典

刪除字典則有三種情況

- 刪除字典中特定元素，語法為：`del 字典名稱[鍵]`
- 刪除字典中所有元素，語法為：`字典名稱.clear()`
- 刪除字典，字典刪除後該字典就不存在，語法為：`del 字典名稱`

---

### 字典常用的進階功能

字典常用的進階功能整理於下表：( 表中 dict1={"joe":5, "mary":8}，n 為整數，b 為布林變數)

| 方法                    | 說明                              | 範例及結果                                                 |
|-----------------------|---------------------------------|-------------------------------------------------------|
| len(dict1)            | 取得字典元素個數                        | n=len(dict1)</br>n=2                                  |
| dict1.copy()          | 複製字典                            | dict2=dict1.copy()</br>dict2={"joe":5, "mary":8}      |
| 鍵 in dict1            | 檢查鍵是否存在                         | b="joe" in dict1</br>b=True                           |
| dict1.items()         | 取得以「鍵-值」組為元素的組合                 | item1=dict1.items()</br>dict2=[("joe",5),("marry",8)] |
| dict1.keys()          | 取得以「鍵」為元素的組合                    | key1=dict1.keys()</br>key1=['joe', 'mary']            |
| dict1.setdefault()    | 與get()類似，若「鍵」不存在就以參數的「鍵-值」建立新元素 | n=dict1.setdefault("joe")</br>n=5                     |
| value1=dict1.values() | 取得以「值」為元素的組合                    | value1=dict1.values()</br>value1=[5,8]                |

---

### in 功能

- 許多字典功能傳送「鍵」做為參數時，若做為參數的「鍵」不存在就會產生錯誤而讓程式中斷執行。
- in 功能會檢查字典中的「鍵」是否存在，語法為：`鍵 in 字典名稱`
- 如果「鍵」存在就傳回 True，「鍵」不存在就傳回 False。
- in 功能可在執行如果「鍵」不存在就會產生錯誤的程式之前進行檢查， 確定「鍵」存在才執行該程式。

[08_in.py][08_in.py]

---

### keys 及 values 功能

- 字典的 keys() 功能可取得字典中所有「鍵」，資料型態為 dict_keys，雖然 dict_keys 資料型態看起來像串列，但它不能以索引方式取得元素值：

```pytho
dict1={"香蕉":20, "蘋果":50, "橘子":30}
key1 = dict1.keys()
print(key1[0]) #TypeError: 'dict_keys' object is not subscriptable
```

- 必須將 dict_keys 資料型態以 list 函式轉換為串列才能取得元素值：

```python
dict1={"香蕉":20, "蘋果":50, "橘子":30}
key1 = list(dict1.keys())
print(key1[0]) # 香蕉
```

- values() 功能可取得字典中所有「值」， 資料型態為 dict_values。dict_values 資料型態的用法與 dict_keys 完全相同。

[09_keyvalue.py][09_keyvalue.py]

---

### items 功能

- items() 功能可同時取得所有「鍵- 值」組成的組合，資料型態為 dict_items。
- 將 dict_items 資料型態以 list 函式轉換為串列後相當於二維串列，可以取得個別元素值。

[10_item.py][10_item.py]

---

### 練習題 2

不同星座的人有不同的性格特徵。『鍵』為星座名稱，『值』為性格特徵。利用items功能顯示星座名稱及該星座的性格特徵。

---

## 字串的操作

### 連接及分割字串

#### join 函式

join 函式可將串列中元素連接組成一個字串。

語法為：連接字串.join(串列)

join 函式會在元素之間插入「連接字串」來組成一個字串

---

#### split 函式

split 函式的功能與join 函式相反，是將一個字串以指定方式分割為串列。

語法為：字串.split([分隔字串])

「分隔字串」可有可無，若未傳入分隔字串，其預設值為 1 個空白字元

[13_split.py][13_split.py]

---

### 檢查起始或結束字串

#### startswith 函式

startswith 函式是檢查字串是否以指定字串開頭。

語法為：字串.startswith(起始字串)

如果字串是以「起始字串」開頭就傳回 True，否則就傳回 False

#### endswith 函式

endswith 函式的功能與 startswith 函式雷同，只是 endswith 函式檢查的是字串是否以指定字串結束。

語法為：字串.endswith(起始字串)

如果字串是以「結尾字串」結束就傳回 True，否則就傳回 False

[14_startswith.py][14_startswith.py]

---

### 移除前後空白字元

#### lstrip、rstrip 及 strip 函式

lstrip 函式可移除字串左方的空白字元。

語法為：字串.lstrip()

rstrip 函式可移除字串右方的空白字元，strip 函式則是同時移除字串左、右方的空白字元。注意：在文字之間的空白字元不會移除。

[15_strip.py][15_strip.py]

---

### 搜尋及取代字串

#### find 函式

- find 函式是尋找搜尋字串在字串的位置。

- 語法為：字串.find(搜尋字串)

- 執行結果是搜尋字串在字串中的位置，注意位置是由「0」開始計數。如果搜尋字串在字串中不存在，會傳回「-1」。

---

#### replace 函式

- replace 函式是將字串中特定字串替換為另一個字串。

- 語法為：字串.replace(被取代字串,取代字串[,最大次數])

- 「最大次數」為最多取代次數。 如果省略「最大次數」，則字串中所有「被取代字串」都會替換為「取代字串」。

- 如果將「取代字串」設為空字串 ("")，其效果就是移除字串中的「被取代字串」。

[16_find_replace.py][16_find_replace.py]

---

## 函式

### 自訂函式

- Python 是以 def 命令建立函式，可以傳送多個參數給函式，執行完函式後也可返回多個回傳值。自行建立函式的語法為：

```python
def 函式名稱(參數1, 參數2, ...):
    程式區塊
    return 回傳值1, 回傳值2, ...
```

- 參數 ( 參數 1, 參數 2, ……) ：參數可以傳送一個或多個，也可以不傳送參數。如果有多個參數，則參數之間必須用逗號「,」分開。
- 回傳值 ( 回傳值 1, 回傳值 2, ……) ：回傳值可以是一個或多個，也可以沒有回傳值。回傳值是執行完函式後傳回主程式的資料，若有多個回傳值，則回傳值之間必須用逗號「,」分開，主程式則要有多個變數來接收回傳值。

---

- 函式建立後並不會執行，必須在主程式中呼叫函式，才會執行函式，呼叫函式的語法為：`變數=函式名稱(參數)`

- 如果參數的數量較多，常會搞錯參數順序而導致錯誤結果，呼叫函式時可以輸入參數名稱，此種方式與參數順序無關，可以減少錯誤。不過輸入參數名稱方式會多輸入不少文字，降低建立程式效率。

[11_ctof.py][11_ctof.py]

---

### 數值函式

python常用的數值函式有：

| 函式        | 功能             | 範例             | 結果    |
|-----------|----------------|----------------|-------|
| abs(x)    | 取得x的絕對值        | abs(-5)        | 5     |
| chr(x)    | 取得整數x的字元       | chr(65)        | A     |
| divmod(x) | 取得x除以y的商及餘數的元組 | divmod(44,6)   | (7,2) |
| float(x)  | 將x轉成浮點數        | float("56")    | 56    |
| hex(x)    | 將x轉成十六進位       | hex(34)        | 0x22  |
| int(x)    | 將x轉成整數         | int(34.21)     | 34    |
| len(x)    | 取得元素個數         | len([1,3,5,7]) | 4     |

---

| 函式         | 功能              | 範例             | 結果    |
|------------|-----------------|----------------|-------|
| max(參數串列)  | 取得參數串列中的最大值     | max(1,3,5,7)   | 7     |
| min(參數串列)  | 取得參數串列中的最小值     | min(1,3,5,7)   | 1     |
| oct(x)     | 將x轉成八位數字        | oct(34)        | 0o42  |
| ord(x)     | 回傳字元x的unicode編碼 | ord("我")       | 25105 |
| pow(x,y)   | x的y次方           | pow(2,3)       | 8     |
| round(x)   | 以四捨六入法取得x的近似值   | round(45.8)    | 46    |
| sorted(串列) | 由小到大排序          | len([1,3,5,7]) | 4     |
| str(x)     | 將x轉成字串          | str(56)        | "56"  |
| sum(串列)    | 計算串列元素的總和       | sum([1,3,5,7]) | 16    |

[12_divmod.py][12_divmod.py]

---

### 字串函式

python常用的字串函式有：

| 函式           | 功能                     | 範例                         | 結果               |
|--------------|------------------------|----------------------------|------------------|
| center(n)    | 將字串擴充為n個字元且置中          | "book".center(8)           | "  book  "       |
| rjust(n)     | 將字串擴充為n個字元且靠右          | "book".rjust(8)            | "    book"       |
| ljust(n)     | 將字串擴充為n個字元且靠左          | "book".ljust(8)            | "book    "       |
| strip()      | 移除字串左方及右方的空白字元         | "  book  ".strip()         | "book"           |
| rstrip()     | 移除字串右方的空白字元            | "  book  ".rstrip()        | "  book"         |
| lstrip()     | 移除字串左方的空白字元            | "book".center(8)           | "  book  "       |
| split(s)     | 將字串以s字串為分隔字元分割為串列      | "ab#cd#ef".split("#")      | ["ab","cd","ef"] |
| s.join(list) | 將串列中元素以s字串做為連接字元組成一個字串 | "#".join(["ab","cd","ef"]) | ab#cd#ef         |
| len(字串)      | 取得字串長度                 | len("book")                | 4                |---

---

| 函式             | 功能           | 範例                      | 結果    |
|----------------|--------------|-------------------------|-------|
| replace(s1,s2) | 將字串中的s1以s2取代 | "book".replace("o","a") | baak  |
| find(s)        | 搜尋s字串在字串中的位置 | "book".find("k")        | 3     |
| lower()        | 將字串字元都轉為小寫字母 | "Yes".lower()           | yes   |
| upper()        | 將字串字元都轉為大寫字母 | "Yes".upper()           | YES   |
| startswith(s)  | 字串是否以s字串為開頭  | "abc".startswith("a")   | True  |
| endswith(s)    | 字串是否以s字串結尾   | "abc".endswith("c")     | True  |
| islower()      | 字串是否都為小寫字母   | "Yes".islower()         | False |
| isupper()      | 字串是否都為大寫字母   | "YES".isupper()         | True  |

---

## 模組

### import 模組

#### 第一種語法為：import 模組名稱

模組只要使用「import」命令就可匯入，通常模組中有許多函式供設計者使用，使用這些函式的語法為：套件名稱.函式名稱

---

#### 第二種語法為：from 模組名稱 import *

以此種語法匯入套件後，使用套件函式就不必輸入套件名稱 ( 輸入套件名稱也可以)，直接使用函式即可。

此種方法雖然方便，卻隱藏著極大風險：每一個套件擁有眾多函式，若兩個套件具有相同名稱的函式，由於未輸入套件名稱，使用函式時可能造成錯誤。

---

#### 第三種語法為：import 模組名稱 as 別名

為兼顧便利性及安全性，可為套件名稱另取一個簡短的別名。
這樣一來，使用函式時就用「別名. 函式名稱」呼叫，既可避免輸入較長的套件名稱，又可避免不同套件中相同函式名稱問題。

---

### 亂數模組函式整理

要使用亂數功能需先匯入亂數套件，匯入亂數套件且設別名為「r」的程式為：import random as r

---

常用的亂數模組有：
| 函式                  | 功能                     | 範例                  | 結果               |
|---------------------|------------------------|---------------------|------------------|
| choice(字串)          | 由字串中隨機取得一個字元           | r.choice(str1)      | b                |
| randint(n1,n2)      | 由n1到n2之間隨機取得一個整數       | r.randint(1,10)     | 7                |
| random()            | 由0到1之間取得一個浮點數          | r.random()          | 0.8933421…       |
| randrange(n1,n2,n3) | 由n1到n2之間每隔n3的數隨機取得一個整數 | r.randrange(0,11,2) | 8                |
| sample(字串, n)       | 由字串中隨機取得n個字元           | r.sample(str1,3)    | ['c','a','d']    |
| shuffle(串列)         | 為串列洗牌                  | r.shuffle(list1)    | ['ef','ab','cd'] |
| uniform(f1,f2)      | 由f1到f2之間隨機取得一個浮點數      | r.uniform(f1,f2)    | 6.351865….       |

---

### 產生整數或浮點數的亂數函式

#### randint 函式

- randint 函式的功能是由指定範圍產生一個整數亂數。

- 語法為：亂數套件別名.randint(起始值,終止值)

- 執行後會產生一個在起始值 (含) 和終止值 (含) 之間的整數亂數。

#### random 函式

- random 函式的功能是產生一個 0 到 1 之間的浮點數亂數。

- 語法為：亂數套件別名.random()

[17_randint.py][17_randint.py]

---

### 隨機取得字元或串列元素

#### choice 函式

- choice 函式的功能是隨機取得一個字元或串列元素。
- 語法為：亂數套件別名.choice(字串或串列)
- 如果參數是字串，就隨機由字串中取得一個字元。
- 如果參數是串列，就隨機由串列中取得一個元素。

---

#### sample 函式

- sample 函式的功能與 choice 雷同，可以隨機取得多個字元或串列元素。
- 語法為：亂數套件別名.sample(字串或串列,數量)
- 如果參數是字串，就隨機由字串中取得指定數量的字元；如果參數是串列，就隨機由串列中取得指定數量的元素。
- sample 函式最重要的用途是可以由串列中取得指定數量且不重複的元素，這使得設計樂透開獎應用程式變得輕鬆愉快。

[18_sample.py][18_sample.py]

---

### 時間模組

Python中常用的時間模組函式有
| 函式                | 功能                |
|-------------------|-------------------|
| clock()           | 取得程式執行時間          |
| ctime([時間數值])     | 以傳入的時間數值來取得時間字串   |
| localtime([時間數值]) | 以傳入的時間數值來取得時間元組資訊 |
| sleep(n)          | 程式執行n秒            |
| time()            | 取得目前時間數值          |

要使用時間功能需先匯入時間套件，匯入時間套件且設別名為「t」的程式為：import time as t

---

### 取得時間訊息函式

#### time 函式

- Python 的時間是以 tick 為單位，長度為百萬分之一秒 ( 微秒)。Python 計時是從 1970 年 1 月1 日零時開始的秒數，此數值即為「時間數值」，是一個精確到小數點六位數的浮點數，time 函式可取得此時間數值。
- 語法為：時間套件別名.time()

#### localtime 函式

- localtime 函式可以取得使用者時區的日期及時間資訊。
- 語法為：時間套件別名.localtime([時間數值])
- 「時間數值」參數可有可無， 若省略「時間數值」參數則是取得目前日期及時間，返回值是以元組資料型態傳回。

---

#### ctime 函式

- ctime 函式的功能及用法皆與 localtime 函式相同，不同處在於 ctime 函式的傳回值為字串。
- 語法為：時間套件別名.ctime([時間數值])
- ctime 函式的傳回值格式為：`星期 月份 日數 時:分:秒 西元`

[19_time.py][19_time.py]

#### sleep 函式

- sleep 函式可讓程式休息一段時間，即程式停止執行一段時間。
- 語法為：時間套件別名.sleep(休息時間)
- 「休息時間」的單位為「秒」 。

---

### 練習題

猜拳。

1剪刀、2石頭、3布，與電腦猜拳，並統計輸贏的次數。

---

## 檔案處理

### 開啟檔案

語法：open(filename, mode, encode)
open() 函式中最常使用的參數是 filename、mode 和 encode，其中只有參數 filename 是必填，其他參數省略時會使用預設值。開啟檔案有三種模式：

- r ：讀取模式，此為預設模試。
- w ：寫入模試，若檔案已存在，內容將會被覆蓋。
- a ：附加模試，若檔案已存在，內容將會被加至尾端。

---

使用 open 函式時會建立一個物件，利用這個物件就可以處理檔案，檔案處理結束要以 close 方法關閉檔案。

```python
f=open('file1.txt','r')
...
f.close()
```

[20_filewrite.py][20_filewrite.py]

[21_fileread1.py][21_fileread1.py]

---

### 使用with...as 語法

可以使用with...as 語法來簡化，語法結束後自動關閉開啟的檔案

[22_fileread2.py][22_fileread2.py]

---

### 設定檔案的編碼

- 使用 open() 函式預設的文件編碼會依作業系統而定，如果是繁體中文Windows 系統，預設的編碼是 cp950 (Big-5)。

- 指定讀取檔案的編碼
    如果想要以Windows 預設的編碼方式來讀取檔案，可以用：

    `f=open("file1.txt", "r")`

    或明確指定檔案編碼是 UTF-8。

    `f=open("file1.txt", "r",encoding= "utf-8")`

---

### 常用處理檔案內容的方法

| 方法           | 說明                         |
|--------------|----------------------------|
| close()      | 關檔                         |
| flush()      | 強迫將緩衝區的資盼拉即寫入檔案履，並清除緩衝區。   |
| read([size]) | 讀取指定長度的字元，如果未指定長度則會讀取所有字元。 |
| readable()   | 測試是否可讀取                    |
| readlines()  | 讀取所有列，它會傳回一個串列。            |
| next()       | 移到下一列                      |
| seek(0)      | 將指標移到文件最前端                 |
| tell()       | 傳回文件門前位置                   |
| write(str)   | 將指定的字串寫入文件中，它沒有傳回值。        |
| writable()   | 測試是否可寫入                    |

[23_readlines.py][23_readlines.py]

---

### 練習題 3

開啟文字檔，讀取所有資料並在每行的前面加上編號並輸出，最後計算文章共有幾個字。

---

## 例外處理

大部分執行中的錯誤， Python 直譯器會以發起例外 (exception) 的方式來中斷程式的執行。

很多情況下我們需要自行控制可能會產生例外的程式碼，這種情況下，我們需要的是例外發生後的處理動作，而非中止程式的執行。

---

### try...except...finally 使用方式

- 最簡單方式：try...except

    ```python
    try:
        print(n)
    except:
        print("變數 n 不存在!")
    ```

[24_try1.py][24_try1.py]

- 若加入except的參數，就可以觀察錯誤訊息：

    ```python
    try:
        print(n)
    except Exception as e:
        print("變數 n 不存在!") # name 'n' is not defined
    ```

[25_try2.py][25_try2.py]

---

- 若加入另一個關鍵字 finally，無論例外有沒有發生都會執行 finally 後的程式區塊：

    ```python
    try:
        print(n)
    except Exception as e:
        print("變數 n 不存在!") # name 'n' is not defined
    finally:
        print("一定會執行的程式區塊")
    ```

[26_try3.py][26_try3.py]

---

### 練習題 4

輸入兩個正整數，求兩數之和。程式中，若輸入非數值資料，以 try⋯except 捕捉發生的錯誤。

[02_串列元素配置]: icons/02_串列元素配置.png
[02_串列元素內容]: icons/02_串列元素內容.png
[02_字典元素配置]: icons/02_字典元素配置.png
[01_list1.py]: https://github.com/scchang2023/linkou_community/tree/main/sample_codes/part2/01_list1.py
[02_list2.py]: https://github.com/scchang2023/linkou_community/tree/main/sample_codes/part2/02_list2.py
[03_list3.py]: https://github.com/scchang2023/linkou_community/tree/main/sample_codes/part2/03_list3.py
[04_append.py]: https://github.com/scchang2023/linkou_community/tree/main/sample_codes/part2/04_append.py
[05_remove.py]: https://github.com/scchang2023/linkou_community/tree/main/sample_codes/part2/05_remove.py
[06_sorted.py]: https://github.com/scchang2023/linkou_community/tree/main/sample_codes/part2/06_sorted.py
[07_dictget.py]: https://github.com/scchang2023/linkou_community/tree/main/sample_codes/part2/07_dictget.py
[08_in.py]: https://github.com/scchang2023/linkou_community/tree/main/sample_codes/part2/08_in.py
[09_keyvalue.py]: https://github.com/scchang2023/linkou_community/tree/main/sample_codes/part2/09_keyvalue.py
[10_item.py]: https://github.com/scchang2023/linkou_community/tree/main/sample_codes/part2/10_item.py
[11_ctof.py]: https://github.com/scchang2023/linkou_community/tree/main/sample_codes/part2/11_ctof.py
[12_divmod.py]: https://github.com/scchang2023/linkou_community/tree/main/sample_codes/part2/12_divmod.py
[13_split.py]: https://github.com/scchang2023/linkou_community/tree/main/sample_codes/part2/13_split.py
[14_startswith.py]: https://github.com/scchang2023/linkou_community/tree/main/sample_codes/part2/14_startswith.py
[15_strip.py]: https://github.com/scchang2023/linkou_community/tree/main/sample_codes/part2/15_strip.py
[16_find_replace.py]: https://github.com/scchang2023/linkou_community/tree/main/sample_codes/part2/16_find_replace.py
[17_randint.py]: https://github.com/scchang2023/linkou_community/tree/main/sample_codes/part2/17_randint.py
[18_sample.py]: https://github.com/scchang2023/linkou_community/tree/main/sample_codes/part2/18_sample.py
[19_time.py]: https://github.com/scchang2023/linkou_community/tree/main/sample_codes/part2/19_time.py
[20_filewrite.py]: https://github.com/scchang2023/linkou_community/tree/main/sample_codes/part2/20_filewrite.py
[21_fileread1.py]: https://github.com/scchang2023/linkou_community/tree/main/sample_codes/part2/21_fileread1.py
[22_fileread2.py]: https://github.com/scchang2023/linkou_community/tree/main/sample_codes/part2/22_fileread2.py
[23_readlines.py]: https://github.com/scchang2023/linkou_community/tree/main/sample_codes/part2/23_readlines.py
[24_try1.py]: https://github.com/scchang2023/linkou_community/tree/main/sample_codes/part2/24_try1.py
[25_try2.py]: https://github.com/scchang2023/linkou_community/tree/main/sample_codes/part2/25_try2.py
[26_try3.py]: https://github.com/scchang2023/linkou_community/tree/main/sample_codes/part2/26_try3.py
