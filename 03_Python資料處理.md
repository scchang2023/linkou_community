---
# theme: sky
# width: 1280
# height: 960
# marp: true
---

# Python</br>資料處理

章士祺

---

## CSV檔案格式

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

### 寫入Dictionary

### 練習題 1

## JSON檔案格式

[01_csvread.py]: /sample_codes/part3/01_csvread.py
[02_csvreaddict.py]: /sample_codes/part3/02_csvreaddict.py
