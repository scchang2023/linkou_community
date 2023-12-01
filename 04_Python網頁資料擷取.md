# Python</br>網頁資料擷取

章士祺

[TOC]

---

### 網頁資料擷取

- 網頁資料擷取是一種從網頁上取得頁面內容的電腦軟體技術。
- 通常透過軟體使用低階的超文字傳輸協定模仿人類的正常存取。
- 著重於轉換網路上非結構化資料（常見的是HTML格式）成為能在資料庫和電子試算表中儲存和分析的結構化資料。

---

### 網頁資料擷取過程

1. 存取網站取得內容

    可以urllib或requests等網站存取套件存取網站內容。

1. 解析取得內容

    可以配合re正規表示式匹配工具、BeautifulSoup網頁解析套件、Selenium套件。

1. 處理資料

   可以利用資料分析或資料視覺化工具進行資料處理與展示。

---

### requests套件

- requests套件為第三方套件
- 使用requests套件的get()函式，可以讀取網頁的資料，其語法如下：get(網址)
- get()函式會對伺服器(Server)提出取得網頁資料的請求(Request)，伺服器接到請求後，回應(Response)網頁的原始碼內容。

[01_requests1.py][01_requests1.py]
[02_requests2.py][02_requests2.py]

---

### BeautifulSoup套件

- BeautifulSoup套件為第三方套件
- 目前BeautifulSoup套件已經發展到第4版，簡稱bs4，匯入BeautifulSoup套件的語法如下：from bs4 import BeautifulSoup。
- BeautifulSoup套件與requests套件可以整合運用，由requests套件取得網頁的原始碼，然後在BeautifulSoup套件中運用html.parser解析原始碼，自訂bs為BeautifulSoup型別物件名稱，其語法如下： bs=BeautifulSoup (原始碼，"html.parser")。

---

### BeautifulSoup套件常見屬性或函式

| 屬性或函式          | 說明                                                                               | 範例                    |
|----------------|----------------------------------------------------------------------------------|-----------------------|
| title          | 取得網頁的標題                                                                          | bs.title              |
| text           | 取得網頁去除html標籤後的內容                                                                 | bs.text               |
| find("標籤")     | 找出第一個符合指定條件的html標籤，其回傳值為字串，如果找不到資料則回傳「None」                                      | bs.find("a")          |
| find_all("標籤") | 找出所有符合指定條件的html標籤，其回傳值為串列，如果找不到資料則回傳「None」                                       | bs.find_all("a")      |
| select()       | 找出指定的CSS選擇器之id或class的內容，id名稱前要加上「#」符號，class名稱前要加上「.」符號，其回傳值為字串，如果找不到資料，則回傳「None」 | bs.select("#id名稱")    |
|                |                                                                                  | bs.select(".class名稱") |
|                |                                                                                  | bs.select("標籤")       |

---

### 網路爬蟲常用標籤

- `<head>`：表示網站的開頭部分。
- `<body>`：定義網頁檔案之主體。
- `<div>`：定義網頁檔案的一個區塊，裡面可以包含很多元素。
- `<title>`：定義網頁標題名稱（顯示於視窗標題和分頁之名稱）。
- `<h1>`：定義HTML內文標題1(最高級)標題，通常也是標題中最重要的。
- `<a href>`：定義超連結，跟著href屬性一起合用。
- `<form>`：定義用於使用者輸入之HTML表單。
- `<tr>` / `<td>` ：定義表格時最常用的兩個標籤，`<tr>` 是列， `<td>` 則是欄。

---

### 網路爬蟲常用屬性及函式

- 屬性：

    id：獨一無二的代表網頁。

    class：描述類似的元素的歸類。

    href：超連結，有超連結我們就可以繼續深入下一個連結。
- 函式：

    find( )函式與find_all( )函式，可以搭配屬性名稱與屬性內容，讀取出符合屬性的標籤資料，其語法如下：
    `find_all("標籤",{"屬性名稱"："屬性內容"})`

[03_bs4.py][03_bs4.py]

---

### 範例 1：台銀牌告匯率

https://rate.bot.com.tw/xrt?Lang=zh-TW

![Alt text][04_台銀牌告匯率]

---

#### 檢視網頁原始碼

![Alt text][04_台銀牌告匯率_網頁原始碼]

[04_tbank.py][04_tbank.py]

---

### 範例 2：大樂透

https://www.taiwanlottery.com.tw/result_all.htm

![Alt text][04_台彩大樂透]

[05_lottery.py][05_lottery.py]

---

### 範例3：網路擷取圖片

https://www.edu.tw/Default.aspx

![Alt text][04_教育部]

[06_pic.py][06_pic.py]

---

### 練習題 1

自行選定目標網頁進行爬取。例如：統一發票開獎。

---

[01_requests1.py]: /sample_codes/part4/01_requests1.py
[02_requests2.py]: /sample_codes/part4/02_requests2.py
[03_bs4.py]: /sample_codes/part4/03_bs4.py
[04_tbank.py]: /sample_codes/part4/04_tbank.py
[05_lottery.py]: /sample_codes/part4/05_lottery.py
[06_pic.py]: /sample_codes/part4/06_pic.py

[04_台銀牌告匯率]: /icons/04_台銀牌告匯率.png
[04_台銀牌告匯率_網頁原始碼]: /icons/04_台銀牌告匯率_網頁原始碼.png
[04_台彩大樂透]: /icons/04_台彩大樂透.png
[04_教育部]: /icons/04_教育部.png
