---
# theme: sky
# width: 1280
# height: 960
# marp: true
---
# Python</br>基本語法介紹

章士祺

---

## 開發環境

### 安裝 Python

https://www.python.org/

---

### 安裝 Visual Studio Code

https://code.visualstudio.com/

---

### 寫第一隻程式測試

印出 Hello Python

執行程式

---

### 註解

- 單行註解：Python可在程式碼中加入`#`做為單行註解，例如：

```python
# 這是單行註解
```

- 多行註解：在註解的區塊前後加入三個單引號 `'''` 或三個雙引號 `"""` 作為多行註解，例如：

```python
'''
第一行註解
第二行註解
第三行註解
'''
```

---

## 變數

- 變數是用來儲存資料的自訂名稱。

- 新增變數：Python 的變數不需要宣告就可以使用了，語法為：`變數名稱 = 變數值`

- 如果多個變數具有相同數值，可以一起指定變數值，例如：`a=b=c=30`

- 可以在同一列指定多個變數，變數之間以「`，`」分隔，值之間也以「`，`」分隔，例如：`name,age="小明",20`

- 刪除變數：如果變數不再使用，可以刪除，語法為：`del 變數名稱`

---

### 變數命名規則

- 變數的名稱只能以英文字母（`A-Z, a-z`）、數字（`0-9`）以及底線（`_`）所組成。

- 變數名稱不得以數字開頭。

- 英文字母大小寫視為不同變數名稱。

- 變數名稱不能與 Python 內建的保留字相同。

```python !
False, None, True, and, as, assert, async, await, break, class, continue, def, del, elif, else, except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield
```

---

## 資料型態

### 數值

- 整數 `int`：不包含小數點的數值。

- 浮點數 `float`：包含小數點的數值。

- 布林 `bool`：只有兩個值：`True`，`False`。

---

### 字串

Python 字串（`str`）是變數值以一對雙引號「`"`」或單引號 「`'`」包起來，例如：
  
```python
str1 = "這是字串"
```

如果字串要包含引號（雙引號或單引號），可使用另一種引號包住字串，例如：

```python
str2 = "小明說 '您好' "
str3 = '小花說 "早上好" '
```

---

### `type` 命令

type 命令可以取得變數的資料型態，如果不確定變數的型態，可用 type 來查看，語法：`type(變數)`，例如：

```python
print(type(23))             # <class 'int'>
print(type(25.0))           # <class 'float'>
print(type("Good moring!")) # <class 'str'>
print(type(True))           # <class 'bool'>
```

---

### 資料型態轉換

Python 具有簡單的資料型態自動轉換功能：如整數與浮點運算，系統會先將整數轉換為浮點數再運算，運算結果為浮點數，例如：`num=5+7.8`

Python 強制資料型態轉換：

- `int()`：強制轉換為整數資料型態。
- `float()`：強制轉換為浮點數資料型態。
- `str()`：強制轉換為字串資料型態。

---

## 輸出

### `print` 輸出命令

- print 命令能列印指定變數的內容，語法為：
`print(變數1,變數2,...,sep=分隔字元,end=結束字元)`

- `變數1, 變數2, ...`：print 命令可以一次列印多個變數資料，變數之間以逗號「`,`」分開。

- `sep`：分隔字元，如果列印多個變數，變數之間以分隔符號區隔，預設值為一個空白字元 (" ")。

- `end`：結束字元，列印完畢後自動加入的字元，預設值為換列字元("`\n`")，所以下一次執行 print 命令會列印在下一列。

[02_print.py][02_print.py]

---

### 「`%`」參數格式化

- print 命令支援參數格式化功能，語法為：`print(format_string % data)`

常用的參數有：
|型態|說明|
|:-:|:-|
|`%%`|在字串中顯示%|
|`%d`|以整數資料型態輸出|
|`%f`|以浮點數資料型態輸出|
|`%s`|以字串資料型態輸出|
|`%e`或`%E`|以科學記號方式輸出|

[03_printf.py][03_printf.py]

---

- 精確控制列印位置，讓出資料排列更整齊。

- `%5d`：固定列印5個字元，若少於5位數，會在數字填入空白字元。

- `%5s`：固定列印5個字元，若字串少於5個字元，會在字串左方填入空白字元。

- `%6.3f`：固字列定6個字元（含小數點），小數固定列印2位數。若整數小於2位數，會在左方填入空白字元，若小數小於2位數，會在數字右方填入「0」字元。

[04_printf2.py][04_printf2.py]

---

### format 格式化輸出

利用 format 方法，以一對大括號 `{}` 表示參數的位置。

```python
print("{} {}".format("hello", "world"))  
print("{0} {1}".format("hello", "world"))  
print("{1} {0} {1}".format("hello", "world"))
```

[05_format.py][05_format.py]

---

### f-string 格式化字串

我們可以在字串前加上字母 "`f`" 或 "`F`"，然後使用大括號 "`{}`" 包含變數或表達式。這些大括號內的內容將被替換為對應變數或表達式的值。

[06_fstring.py][06_fstring.py]

---

### 練習題 1

請使用格式化輸出或f-string的方法，將學生的姓名、數學成績、英語成績、以及總分統計輸出。變數名稱：`name="Kerry"`、`math=70`、`eng=95`，輸出格式如下。

```python
學生姓名：Kerry
數學成績：70
英語成績：95
總分　　：165
```

---

## 輸入

### `input` 輸入命令

語法：`變數 = input(提示字串)`

提示字串是輸出一段訊息，告知使用者如何輸入。

```python
chinese = int(input("請輸入國文成績: "))
math = int(input("請輸入數學成績: "))
english = int(input("請輸入英文成績: "))
```

[07_input.py][07_input.py]

---

## 運算式

- 指定資料做哪一種運算的是運算子

- 進行運算的資料是運算元，例如：`3 + 5`， `+` 是運算子，`3`、`5` 是運算元。

---

### 算數運算子

|運算子|說明|範例|結果|
|:-|:-|:-|:-|
|`+`|加法|`5+8`|`13`|
|`-`|減法|`90-10`|`80`|
|`*`|乘法|`4*7`|`28`|
|`/`|除法|`7/2`|`3.5`|
|`%`|取得餘數|`7%3`|`1`|
|`//`|取得商數|`7//2`|`3`|
|`**`|次方|`7**2`|`49`|

---

### 比較運算子

|運算子|說明|範例|結果|
|:-|:-|:-|:-|
|`==`|運算式1是否等於運算式2|`6+9==2+13`</br>`8+9==2+13`|`True`</br>`False`|
|`!=`|運算式1是否不等於運算式2|`8+9!=2+13`</br>`6+9!=2+13`|`True`</br>`False`|
|`>`|運算式1是否大於運算式2|`8+9>2+13`</br>`6+9==2+13`|`True`</br>`False`|
|`<`|運算式1是否小於運算式2|`5+9<2+13`</br>`8+9<2+13`|`True`</br>`False`|
|`>=`|運算式1是否大於等於運算式2|`6+9>=2+13`</br>`3+9>=2+13`|`True`</br>`False`|
|`<=`|運算式1是否小於等於運算式2|`3+9<=2+13`</br>`8+9<=2+13`|`True`</br>`False`|

---

### 邏輯運算子

|運算子|說明|範例|結果|
|:-:|:-|:-|:-|
|`not`|傳回與原來比較結果相反的值，即比較結果是True，就傳回False, 比較結果是False，就傳回True。|`not(3>5)`</br>`not(5>3)`|`True`</br>`False`|
|`and`|只有兩個運算元的比較結果都是True，才會傳回True，其餘情況傳回False。|`(5>3)and(9>6)`</br>`(5>3)and(9<6)`</br>`(5<3)and(9>6)`</br>`(5<3)and(9<6)`|`True`</br>`False`</br>`False`</br>`False`|
|`or`|只有兩個運算元的比較結果都是False，才會傳回False，其餘情況傳回True。|`(5>3)and(9>6)`</br>`(5>3)and(9<6)`</br>`(5<3)and(9>6)`</br>`(5<3)and(9<6)`|`True`</br>`True`</br>`True`</br>`False`|

---

### 複合指定運算子

以`i=10`為例
|運算子|說明|範例|結果|
|:-:|:-|:-|:-|
|`+=`|相加後再指定給原變數|`i+=5`|`15`|
|`-=`|相減後再指定給原變數|`i+=5`|`15`|
|`*=`|相乘後再指定給原變數|`i*=5`|`15`|
|`/=`|相除後再指定給原變數|`i/=5`|`15`|
|`%=`|相除得到餘數後再指定給原變數|`i/=5`|`15`|
|`//=`|相除得到商數後再指定給原變數|`i//=5`|`2`|
|`**=`|相加後再指定給原變數|`i**=3`|`1000`|

[08_complex.py][08_complex.py]

---

### 運算子「`+`」的功能

- 運算子「`+`」用於數值運算時是計算兩個運算元的總和。

- 運算子「`+`」用於字串組合時是將兩個運算元的字元組合在一起。

---

### 運算子的優先順序

優先順序高（數字較小）者先執行運算，同一列中的運算子具有相同的優先順序，優先順序相同時是由左至右運算。

|優先順序|運算子|優先順序|運算子|
|:-:|:-|:-:|:-|
|1|`()`小括號|6|`not`|
|2|`+`(正數)、`-`(負數)|7|`and`|
|3|`*`(乘)、`/`(除)、`%`(餘)、`//`(商)|8|`or`|
|4|`+`(加法)、-(減)|9|`=`、`+=`、`-=`、`*=`、`/=`、`//=`、`**=`|
|5|`==`、`!=`、`>`、`<`、`>=`、`<=`|

---

### 練習題 2

- 利用鍵盤輸入兩個整數，透過第三個變數，將兩個整數值交換並輸出。

- 挑戰：不透過第三個變數，完成兩數交換。

---

## 條件判斷

### 單向判斷式（`if⋯`）

「if⋯」為單向判斷式，是 if 指令中最簡單的型態，語法為：

```python
if (條件式):
    程式區塊
```

---

單向判斷式流程圖：

```flow
op_pre=>operation: 前一列程式
cond=>condition: 條件式
op1=>operation: 程式區塊
op_next=>operation: 後一列程式

op_pre->cond
cond(yes)->op1
cond(no)->op_next
op1->op_next
```

[09_password1.py][09_password1.py]

---

### 雙向判斷式（`if⋯else`）

「if⋯else⋯」為雙向判斷式，語法為：

```python
if (條件式):
    程式區塊一
else:
    程式區塊二
```

---

雙向判斷式流程圖：

```flow
op_pre=>operation: 前一列程式
cond=>condition: 條件式
op1=>operation: 程式區塊一
op2=>operation: 程式區塊二
op_next=>operation: 後一列程式

op_pre->cond
cond(yes)->op1
cond(no)->op2
op1->op_next
op2->op_next
```

[10_password2.py][10_password2.py]

---

### 多向判斷式（`if⋯elif⋯else`）

「if⋯elif⋯else」的語法為：

```python
if (條件式一):
    程式區塊一
elif (條件式二):
    程式區塊二
elif (條件式三):
    …         
else:
    程式區塊else
```

---

多向判斷式流程圖：

```flow
op_pre=>operation: 前一列程式
cond1=>condition: 條件式一
cond2=>condition: 條件式二
op1=>operation: 程式區塊一
op2=>operation: 程式區塊二
op_else=>operation: 程式區塊else
op_next=>operation: 後一列程式

op_pre->cond1
cond1(yes)->op1
cond1(no)->cond2
cond2(yes)->op2
cond2(no)->op_else
op1->op_next
op2->op_next
op_else->op_next
```

[11_grade.py][11_grade.py]

---

## 迴圈

### `range` 函式

- 用來處理重覆事件的命令稱為「迴圈」

- 迴圈命令有2個：for迴圈，用於執行固定次數的迴圈；while迴圈：沒有固定次數。

- 迴圈最常使用整數循序數列，例如「1,2,3,⋯⋯」，**range 函式的功能就是建立整數循序數列**。

---

### `range` 函式的語法

- range 函式單一參數

  語法為：`數列變數=range(正數值)`，例如：`list1=range(5)  #數列為0,1,2,3,4`

- range 函式二個參數
  
  語法為：`數列變數=range(起始值,終止值)`，例如：`list2=range(3,8)   #數列值為3,4,5,6,7`

  起始值及終止值皆可為負整數，例如：`list3=range(-2,4)   #數列值為-2,-1,0,1,2,3`

---

- range 函式三個參數
  
  語法為：`數列變數=range(起始值,終止值,間隔值)`，例如：
  `list4=range(3,8,1) #數列值為3,4,5,6,7`
  `list5=range(3,8,2) #數列值為3,5,7`

  間隔值也可為負整數，此時起始值必須大於終止值，例如：
  `list6=range(8,3,-1) #數列值為8,7,6,5,4`

---

### `for` 迴圈

語法：

```python
for 變數 in 數列:
    程式區塊
```

以實例解說：

```python
for n in range(3): #產生 0,1,2 的數列
    print(n, end=",") # 執行結果為 0,1,2, 
```

---

流程圖如下：

```flow
op_start=>operation: for迴圈開始
cond=>condition: 條件式
op1=>operation: 程式區塊
op_end=>operation: for迴圈結束

op_start->cond
cond(yes)->op1
cond(no)->op_end
op1->cond
```

[12_numtotal.py][12_numtotal.py]

---

### 巢狀 `for` 迴圈

利用兩層 for 迴圈列印九九乘法表

[13_ninenine.py][13_ninenine.py]

---

### `break` 命令

例如：

```python
for i in range(1, 11):
    if i==6:
        break
    print(i, end=",") # 1,2,3,4,5
```

[14_multiple.py][14_multiple.py]

---

### `continue` 命令

例如：

```python
for i in range(1, 11):
    if i==6:
        continue
    print(i, end=",") # 1,2,3,4,5,7,8,9,10,
```

[15_except5.py][15_except5.py]

---

### while 迴圈

語法：

```python
while(條件式):
    程式區塊
```

流程圖：

```flow
op_start=>operation: while迴圈開始
cond=>condition: 條件式
op1=>operation: 程式區塊
op_end=>operation: while迴圈結束

op_start->cond
cond(yes)->op1
cond(no)->op_end
op1->cond
```

---

例如：

```python
total=n=0
while n<10:
    n += 1
    total+=n
print(total)
```

在使用while迴圈時，要注意設定條件判斷的中止條件，否則會陷入無窮迴圈。

[16_while.py][16_while.py]

---

### 練習題 3

- 輸入正整數N，判斷N是否為質數。
- 輸入正整數N，印出小於N的所有質數

---

### 練習題 4

猜密碼。

玩法：其中一人做莊，給定一個數字範圍，再從中選出一個自然數，此數字稱為「密碼」，不能讓其他參與遊戲者得知。而遊戲參與者輪流猜測數字。每猜一個數，莊家就要告知遊戲者該數字是大於或小於密碼，直至密碼被猜中。

[02_print.py]:https://github.com/scchang2023/linkou_community/tree/main/sample_codes/part1/02_print.py
[03_printf.py]:https://github.com/scchang2023/linkou_community/tree/main/sample_codes/part1/03_printf.py
[04_printf2.py]:https://github.com/scchang2023/linkou_community/tree/main/sample_codes/part1/04_printf2.py
[05_format.py]:https://github.com/scchang2023/linkou_community/tree/main/sample_codes/part1/05_format.py
[06_fstring.py]:https://github.com/scchang2023/linkou_community/tree/main/sample_codes/part1/06_fstring.py
[07_input.py]:https://github.com/scchang2023/linkou_community/tree/main/sample_codes/part1/07_input.py
[08_complex.py]:https://github.com/scchang2023/linkou_community/tree/main/sample_codes/part1/08_complex.py
[09_password1.py]:https://github.com/scchang2023/linkou_community/tree/main/sample_codes/part1/09_password1.py
[10_password2.py]:https://github.com/scchang2023/linkou_community/tree/main/sample_codes/part1/10_password2.py
[11_grade.py]:https://github.com/scchang2023/linkou_community/tree/main/sample_codes/part1/11_grade.py
[12_numtotal.py]:https://github.com/scchang2023/linkou_community/tree/main/sample_codes/part1/12_numtotal.py
[13_ninenine.py]:https://github.com/scchang2023/linkou_community/tree/main/sample_codes/part1/13_ninenine.py
[14_multiple.py]:https://github.com/scchang2023/linkou_community/tree/main/sample_codes/part1/14_multiple.py
[15_except5.py]:https://github.com/scchang2023/linkou_community/tree/main/sample_codes/part1/15_except5.py
[16_while.py]:https://github.com/scchang2023/linkou_community/tree/main/sample_codes/part1/16_while.py