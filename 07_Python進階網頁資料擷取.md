# Python進階網頁資料擷取

章士祺

[TOC]

---

### Selenium：瀏覽器自動化操作

- 一般情況下，我們都是以人工操作方式，執行瀏覽器上的各項操作。
- 事實上，只要安裝自動化操作套件，Python就可以代替我們自動執行。

---

### 安裝 Selenium 套件

在Console視窗中，輸入 `pip install selenium`。

![Alt text](.\icons\07_安裝selenium套件.png)

---

### 下載 Chrome WebDriver

- 下載網址：<http://chromedriver.chromium.org/downloads>
- 確認自己電腦使用 Chrome 的版本
- 選擇Chrome版本並下載
- 解壓縮後，放在與程式碼相同資料夾

---

### Selenium Webdriver 的屬性和方法

Selenium Webdriver API 常用的屬性和方法如下：
| 方法                    | 說明                                   |
|-----------------------|--------------------------------------|
| current_url           | 取得目前的網址                              |
| page_sourcee          | 讀取網頁的原始碼                             |
| text                  | 讀取元素的內容                              |
| size                  | 傳回元素的大小，例如{'width'=250, 'height'=30} |
| get_window_position() | 取得視窗左上角的位置                           |
| set_window_position() | 設定視窗左上角的位置                           |
| maximize_window()     | 視窗最大化                                |
| get_window_size()     | 取得視窗的高度和寬度                           |
| set_window_size()     | 設定視窗的高度和寬度                           |
| click()               | 單擊按鈕                                 |
| close()               | 關閉瀏覽器                                |
| get(url)              | 連結url網址                              |
| refresh()             | 重新整理畫面                               |
| back()                | 返回上一頁                                |
| forward()             | 下一頁                                  |
| send_keys()           | 以鍵盤輸入                                |
| submit()              | 提交                                   |
| quit()                | 關閉瀏覽器並退出驅動程式                         |

---

[01_selenium.py][01_selenium.py]

---

### 練習題 1

利用Selenium開啟Chrome瀏覽器，依序分別連到google、pchome、政府開放資料平台網頁，中間停留10秒。

---

### 8種基本元素定位方法

- find_element_by_id()：以id查詢符合的元素
- find_element_by_name()：以名稱查詢符合的元素
- find_element_by_class_name()：以類別名稱查詢符合的元素
- find_element_by_tag_name()：以HTML標籤查詢符合的元素
- find_element_by_link_text()：以連結文字查詢符合的元素
- find_element_by_partial_link_text()：以部分連結文字查詢符合的元素
- find_element_by_css_selector()：以CSS選擇器查詢符合的元素
- find_element_by_xpath()：以xpath查詢符合的元素

---

### 新版find_element()用法

- find_element (By.ID, )：以id查詢符合的元素
- find_element(By.NAME, )：以名稱查詢符合的元素
- find_element(By.CLASS_NAME, )：以類別名稱查詢符合的元素
- find_element(By.TAG_NAME, )：以HTML標籤查詢符合的元素
- find_element(By.LINK_TEXT, )：以連結文字查詢符合的元素
- find_element(By_PARTIAL_LINK_TEXT, )：以部分連結文字查詢符合的元素
- find_element(By_CSS_SELECTOR, )：以CSS選擇器查詢符合的元素
- find_element(By.XPATH, )：以xpath查詢符合的元素

註：需要 匯入By
`from selenium.webdriver.common.by import By`

---

以實例說明如下，以下列的 HTML 原始碼，Webdriver 為 browser 為例。

```python
<html>
    <body>
        <h1>Welcome</h1>
        <form id="loginForm">
            <p class="content">Are you sure you want to do this?</p>
            <a href="coninue.html">Continue</a>
            <a href="cancel.html">Cancel</a>
            <input name="username" type="text" />
            <input name="password" type="password" />
            <input name="continue" type="submit" value="Login"/>
            <input name="continue" type="button" value="Clear"/>
        </form>
    </body>
</html>
```

---

- find_element_by_id
`login_form=browser.find_element_by_id('loginForm')`
- find_element_by_name
`username=browser.find_element_by_name('username')`
`password=browser.find_element_by_name('password')`
- find_element_by_xpath
`login_form=browser.find_element_by_xpath("//form[@id='loginForm']")`
`username=browser.find_element_by_xpath("//input[@name='username']")`
- find_element_by_link_text
`continue_link=browser.find_element_by_link_text('Continue')`

---

- find_element_by_partial_link_text
`continue_link=browser.find_element_by_partial_link_text('Conti')`
- find_element_by_tag_name
`heading1=browser.find_element_by_tag_name('h1')`
- find_element_by_class_name
`content=browser.find_element_by_class_name('content')`

---

[02_findlink.py][02_findlink.py]

[03_findname.py][03_findname.py]

---

### 練習題 2

利用Selenium開啟Chrome瀏覽器，開啟Facebook網頁，輸入個人帳號密碼登入。

---

### 擷取網頁內容

- 可以利用driver.page_source，抓取網頁的內容。
- 再搭配BeautifulSoup分析網頁內容。

[04_pagesource.py][04_pagesource.py]

---

### 練習題 3

利用Selenium開啟Chrome瀏覽器，開啟google，輸入搜尋關鍵字，印出搜尋到的30筆以上的資料。

---

### 正規表示式

- 在一長串的文字字串中，如果要尋找指定的文字，可以使用in來搜尋。例如：

``` python
str="Hello World!"
print("World" in str) # True
print("Hi" in str) # False
```

- 如果要搜尋的字串複雜許多，使用in是無法完成的。例如：網站超連結、電子郵件帳號、電話號碼或身分證字號等。
- 這時候就必須使用正規表示式(Regular Expression，簡稱regex)才能達成。

---

- 正規表示式透過一些特殊符號的輔助，可以讓使用者輕易達到搜尋/取代某特定字串的處理程序。
- 網站 <http://pythex.org> 可以用來測試正規表示式的結果是否正確。
- 例如，要用正規表示式描述一串整數數字，可以用[0123456789]+這個表示式，其中的中括號[]會框住一群字元，代表合法的字元群，加號+代表的是重複1次或無限多次。
- 因此，該表示式就可以描述像126706、9902、8等樣式的數字。

---

### 常見的正規表示式功能

| 正規表示式 | 功能說明                   |
|-------|------------------------|
| .     | 代表除了換列 (\n) 以外的所有字元    |
| ^     | 代表輸入列的開始               |
| $     | 代表輸入列的結束               |
| *     | 代表前一個項目 0 次或無限多次       |
| +     | 代表前一個項目 1 次或無限多次       |
| ?     | 代表前一個項目 0 次或 1 次       |
| [abc] | 代表一個符合 a 或 b 或 c 的任何字元 |
| [a-z] | 代表一個符合 a-z 的任何字元       |

---

| 正規表示式  | 功能說明                                 |
|--------|--------------------------------------|
| \      | 代表後面的字元以一般字元處理                       |
| {m}    | 代表前面一個項目必須正好出現 m 數                   |
| {m,}   | 代表前面一個項目出現次數最少 m 次，最多無限次。            |
| {m, n} | 代表前面一個項目出現次數最少 m 次，最多 n 次。           |
| \d     | 一個數字字元，相當於[0123456789]或[0-9]。        |
| ^      | 反運算，例如：[^a-d]代表除了a b c d 外的所有字元。     |
| \D     | 一個非數字字元，相當於[^0-9]。                   |
| \n     | 換列字元                                 |
| \r     | 回首字元                                 |
| \t     | tab 定位字元                             |
| \s     | 空白字元                                 |
| \w     | 一個數字、字母或底線字元、相當於[0-9a-zA-Z]          |
| \W     | 一個非數字、字母或底線字元、相當於[^\w]，即[^0-9a-zA-Z] |

---

| 語法      | 正規表示式                                                          | 範例                    |
|---------|----------------------------------------------------------------|-----------------------|
| 整數      | [0-9]+                                                         | 33025                 |
| 有小數點的實數 | [0-9]+\.[0-9]+                                                 | 75.93                 |
| 英文詞彙    | [a-zA-Z]+                                                      | Python                |
| 變數名稱    | [A-Za-z_][A-Za-z0-9_]*                                         | _pointer              |
| Email   | `^([a-z0-9_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$`                | <test@mail.com>         |
| URL     | `^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$` | <http://e-happy.com.tw> |

---

### 建立正規表示式物件

要使用正規表示式，可以使用Anaconda內建好的re套件，再利用re提供的compile方法建立一個正規表示式物件。語法為：

```python
import re
pat=re.compile("[a-z]+")
```

---

### findall() 方法

- 傳回指定字串中所有符合正規表示式的字串，並傳回一個串列。
- 例如：以 findall方法搜尋「 tem12po」 字串，得到的 [‘tem’, ‘po’] 的串列結果如下：

```python
pat=re.compile("[a-z]+")
m=pat.findall("tem12po")
print(m) # ['tem', 'po']
```

[05_re_findall.py][05_re_findall.py]

---

[06_getEmail.py][06_getEmail.py]

---

### 練習題 4

- 利用正規表示式搜尋網頁上的電話號碼。

---

## The End

---

[01_selenium.py]: /sample_codes/part7/01_selenium.py
[02_findlink.py]: /sample_codes/part7/02_findlink.py
[03_findname.py]: /sample_codes/part7/03_findname.py
[04_pagesource.py]: /sample_codes/part7/04_pagesource.py
[05_re_findall.py]: /sample_codes/part7/05_re_findall.py
[06_getEmail.py]: /sample_codes/part7/06_getEmail.py
