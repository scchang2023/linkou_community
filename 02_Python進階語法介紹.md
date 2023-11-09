---
# marp: true
# theme: gaia
# class: invert
---

# Python</br>進階語法介紹

章士祺

---

## 串列（List）

串列（又稱為「清單」或「列表」），與其他語言的「陣列（Array）」相同，其功能與變數相類似，是提供儲存資料的記憶體空間。

</br></br>![01_串列元素配置](./icons/01_串列元素配置.png)

---

## 串列宣告

### 一維串列宣告

- 一維串列的宣告方式是將元素置於中括號 ([]) 中，每個元素之間以逗號分隔，語法為：`串列名稱=[元素1,元素2,…]`
- 例如：宣告 `score` 串列，其元素內容為 `[1, 2, 3, 4, 5]`。
![01_串列元素內容](./icons/01_串列元素內容.png)

---

- 串列中各個元素資料型態可以相同，也可以不同，例如：

```python
list1=[1, 2, 3, 4, 5]
list2=["香蕉", "蘋果", "橘子"]
list3=[1, "香蕉", True]
```

---

### 空串列宣告

例如：`list4=[]`

### 多維串列宣告

例如以下是二維串列範例：

```python
list5=[["joe","1234"], ["mary","3368"], ["david","abcd"]]
print(list5[1])
print(list5[1][1])
```

---

## 讀取串列元素

- 語法：`串列名稱[索引]`
- 例如：

```python
list1 = [1, 2, 3, 4]
print(list1[0])
```

---

- 索引值是從 0 開始計數。索引值不可超出串列的範圍，否則執行時會產生「list index out of range」錯誤。例如：

```python
list4 = ["香蕉", "蘋果", "橘子"]
print(list4[3]) # IndexError: list index out of range
```

- 索引值可以是負值，表示由串列的最後向前取出， 「-1」表示最後一個元素，「-2」表示倒數第二個元素。同理，負數索引值不可超出串列的範圍，否則執行時會產生錯誤。例如：

```python
list4 = ["香蕉", "蘋果", "橘子"]
print(list4[-4]) # IndexError: list index out of range
```

[01_list1.py](sample_codes/part2/01_list1.py)

---

## 改變串列元素改變串列元素

- 語法為：串列名稱[索引]=元素內容
- 例如：

```python
list1=[1, 2, 3, 4, 5]
print(list1[0])
list1[0] = 9
print(list1[0])
```

---
