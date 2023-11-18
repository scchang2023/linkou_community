---
# theme: sky
# width: 1280
# height: 960
# marp: true
---

# Python</br>資料處理

章士祺

---

## CSV檔案

- CSV檔案格式是以逗號隔開欄位資料(Comma Separated Value，CSV)的文字檔格式。
- 在Python中若要讀取或產生CSV的檔案，可以使用內建的 csv 套件。

---

### CSV檔的讀出

- 使用 csv.reader 讀取出來的資料會是一個二維的串列，裡面就是整張表格的資料。
- 在開啟 csv 檔案時加上了 newline="" 參數，是為了讓資料中包含的換行字元可以正確被解析，所以建議在讀取 csv 檔案時都固定加入這個參數。
- 如果資料欄位之間的分隔字元不是使用預設的逗號，而是其他字元的話，在讀取時就要自行指定欄位的分隔字元。
- 例如：`rows = csv.reader(csvfile, delimiter=":")`

[01_csvread.py][01_csvread.py]

---

### 讀取成 Dictionary

- 可以將 csv 檔案的內容讀取進來之後，轉為 Python 的 dictionary 格式，這樣在存取特定資料時會方便一些。
- 會自動把第一列(row)當作欄位的名稱，將第二列以後的每一列轉為 dictionary，這樣我們就可以使用欄位的名稱來存取資料。
- 可以利用 rows.fieldnames讀取欄位名稱。

[02_csvreaddict.py][02_csvreaddict.py]

---

### CSV檔的寫入

- 如果我們在程式中產生了表格的資料，想要儲存為 csv 檔案，可以使用`writer = csv.writer(csvfile)`。
- 如果要以空白分隔欄位，建立 CSV 檔寫入器 `writer = csv.writer(csvfile, delimiter = " ")`。
- 如果資料是已經整理好的二維表格，也可以使用`writer.writerows(table)`一次就把整張表格寫進 csv 檔案中。

[03_csvwrite.py][03_csvwrite.py]

---

### 寫入Dictionary

如果在 Python 中的資料格式是 dictionary，也可以使用 csv.DictWriter 直接將 dictionary 寫入 csv 檔案中。

[04_csvwritedict.py][04_csvwritedict.py]

---

### 練習題 1

政府資料開放平臺 ： https://data.gov.tw/

下載任一csv 檔，並用Python讀取內容

例如：宜蘭縣旅館名冊.csv

[05_csvex.py][05_csvex.py]

---

## JSON檔案

### JSON 概念

- JSON(JavaScript Object Notation) 。
- 是源於JavaScript的開放資料交換格式 。
- 是JavaScript語言的一個子集 。
- JSON用於描述資料結構，有兩種結構存在：

    物件(object)：一個物件包含一系列非排序的名稱/值對(pair)，一個物件以{開始，並以}結束。每個名稱/值對之間使用:分割。

    陣列 (array)：一個陣列是一個值(value)的集合，一個陣列以[開始，並以]結束。陣列成員之間使用,分割。

---

### JSON 具體的格式

- 名稱/值（pair）：名稱和值之間使用：隔開，一般的形式是：{name:value} 一個名稱是一個字串； 一個值(value)可以是一個字串(string)、一個數值(number)、一個物件(object)、一個布林值(bool)、一個有序列表(array)、或者一個null值。

- 字串：以""括起來的一串字元。
數值：一系列0-9的數字組合，可以為負數或者小數。 還可以用e或者E表示為指數形式。
- 布林值：表示為true或者false。

- 值的有序列表(array)：一個或者多個值用,分割後，使用[、]括起來就形成了這樣的列表，形如：[value, value]

---

### JSON 範例

- 範例一：

    `{"name" : "Anna", "age" : 18, "city": "Taoyuan"}`
- 範例二：

    ```python
    {"familys" : [
        {"name" : "Anna", "age" : 18, "city" : "Taoyuan"}, 
        {"name" : "Don", "age" : 21, "city" : "Tainan"} 
    ] }
    {"familys" : [
        {"name" : "Anna", "age" : 18, "city" : "Taoyuan"}, 
        {"name" : "Don", "age" : 21, "city" : "Tainan"} 
    ] }
    ```

---

### JSON 讀取與寫入

- 在Python中若要讀取或產生JSON的檔案，可以使用內建的 json 套件。

- JSON 套件常用方法：

    `json.dumps()`是將Python中的文件序列化為JSON格式的字串。
    `json.loads()`是將已編碼的JSON字串解碼為Python物件。

[06_jsonloads.py][06_jsonloads.py]
[07_jsondumps.py][07_jsondumps.py]

---

### JSON處理複雜結構

在複雜的結構中，取出使用者有興趣的資料。

---

[01_csvread.py]: /sample_codes/part3/01_csvread.py
[02_csvreaddict.py]: /sample_codes/part3/02_csvreaddict.py
[03_csvwrite.py]: /sample_codes/part3/03_csvwrite.py
[04_csvwritedict.py]: /sample_codes/part3/04_csvwritedict.py
[05_csvex.py]: /sample_codes/part3/05_csvex.py
[06_jsonloads.py]: /sample_codes/part3/06_jsonloads.py
[07_jsondumps.py]: /sample_codes/part3/07_jsondumps.py