# Python其它應用

章士祺

[TOC]

---

### QRCode產生

- 安裝qrcode套件，`pip install qrcode`。
- 利用qrcode.make()產生QRCode。
- 利用img.save()將QRCode存成圖檔。

[01_qrcode_gen.py][01_qrcode_gen.py]

---

### QRCode讀取

- 安裝opencv套件，`pip install opencv-python`。
- 安裝pyzbar套件，`pip install pyzbar`。
- 利用cv2.imread()讀入QRCode檔案。
- 利用pyzbar.decode()，讀取QRCode。(一個圖檔可以包含多個QRCode)

[02_pyzbar.py][02_pyzbar.py]

---

### 從WebCam讀取QRCode

[03_QRCode_Camera.py][03_QRCode_Camera.py]

---

### 傳送 Line 通知

- 使用 Python 程式將訊息透過 LINE所提供的官方帳號「LINE Notify」向 LINE 群組發送訊息提醒
- 至 https://notify-bot.line.me/zh_TW/ 進行登入
- 點選右上方帳號名稱選單中的「個人頁面」

---

- 點選「發行權杖」
- 輸入自訂「權杖名稱」，這邊設定的名稱會在出現在提醒訊息的Title
- 選擇分享的群組後 (先選擇第一個)，按下「發行」，即可取得權杖
- 安裝lineTool套件，`pip install lineTool`
- 使用lineNotify()發送訊息

---

- 安裝lineTool套件，pip install lineTool
- 使用lineNotify()發送訊息

[04_linenotift.py][04_linenotift.py]

---

### 挑戰題

結合WebCam和line notify，設計一個入侵警告系統。

提示

```python
diff_img = cv2.subtract(frame,frame1)
d = np.sum(diff_img)
```

---

### 結巴(jieba)斷詞

- 結巴目的說明：有一篇冗長的文章或是字句，可以重新斷詞。
- 安裝jieba套件，`pip install jieba`
- 利用jieba.cut()斷詞，cut_all參數用來控制模式。
  - `cut_all=True`：全模式
  - `cut_all=False`：精確模式(預設)
- github上有一套繁中詞庫，如果想要切換成繁中詞庫，可以先下載放在程式的資料夾內，接著在斷詞指令前，利用jieba.set_dictionary()切換dictionary即可。

[05_jieba.py][05_jieba.py]

---

### 文字雲 wordcloud

- 文字雲目的：是將字詞或句子以圖像化的方式呈現出來。
- 安裝wordcloud套件，`pip install wordcloud`
- 利用WordCloud()設定中文字型以及背景顏色
- 利用generate()產生文字雲，輸入的資料必須是以空格分開的字詞

![Alt text](.\icons\08_文字雲圖像1.png)

[06_wordcloud.py][06_wordcloud.py]

---

---

[01_qrcode_gen.py]: /sample_codes/part8/01_qrcode_gen.py
[02_pyzbar.py]: /sample_codes/part8/02_pyzbar.py
[03_QRCode_Camera.py]: /sample_codes/part8/03_QRCode_Camera.py
[04_linenotift.py]: /sample_codes/part8/04_linenotift.py
[05_jieba.py]: /sample_codes/part8/05_jieba.py
[06_wordcloud.py]: /sample_codes/part8/06_wordcloud.py