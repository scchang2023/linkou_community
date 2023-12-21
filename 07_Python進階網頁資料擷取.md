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

--
