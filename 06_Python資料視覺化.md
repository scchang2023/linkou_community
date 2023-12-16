# Python</br>資料視覺化

章士祺

[TOC]

---

### 圖表繪製

- Python 除了資料擷取進行分析之外，將相關數據繪製成統計圖表更是它的強項。
- Matplotlib 是 Python 在 2D 繪圖領域使用最廣泛的套件，它能讓使用者很輕鬆地將數據圖形化，並且提供多樣化的輸出格式。
- Matplotlib 功能強大，尤其在繪製各種科學圖形上表現更是優異。

---

### Matplotlib 套件

- 使用 Matplotlib 繪圖首先要匯入 Matplotlib 套件，由於大部分繪圖功能是在「matplotlib.pyplot」中，因此通常會在匯入「matplotlib.pyplot」時設定一個簡短的別名，方便往後輸入，例如將別名取為「plt」：`import matplotlib.pyplot as plt`
- matplotlib.pyplot 的線形圖繪圖方法為 plot，語法為：`套件名稱.plot(x座標, y座標)`
- 繪圖後如果不會自動顯示，可用 show 方法顯示，例如：`plot.show()`

[01_plot1.py][01_plot1.py]

---

### plot 方法參數及圖表設定

plot 繪圖方法，除了 x 坐標串列及 y 坐標串列為必要參數外，還有數十個選擇性參數設定繪圖特性，下面是常用的 4 個選擇性參數：

- color：設定線條顏色，預設為藍色，例如設定線條為紅色：color="red"。
- linewidth or lw：設定線條寬度，預設為 1.0，例如設定線條寬度為 5.0：linewidth=5.0。
- linestyle or ls：設定線條樣式，可能值有「-」( 實線 )、「--」( 虛線 )、「-.」( 虛點線) 及「:」( 點線)，預設為「-」。
- label：設定圖例名稱，例如設定圖例名稱為「money」：label="money"。此屬性需搭配 legend 方法才有效果。

前述 label 屬性設定後，需執行 legend 方法才會顯示：`plot.legend()`

---

### 同時繪製多個圖形

一個圖表中可以繪製多個圖形，通常會先將所有圖形都繪製完成後再顯示，例如繪製 2 個圖形：

```python
listx1 = [1, 5, 7, 9, 13, 16]
listy1 = [15, 50, 80, 40, 70, 50]
plt.plot(listx1, listy1)
listx1 = [2, 6, 8, 11, 14, 16]
listy1 = [10, 40, 30, 50, 80, 60]
plt.plot(listx2, listy2)
plt.show()
```

---

### 圖表設定

- 設定圖表標題、x 及 y 坐標標題的語法分別為：

```python
套件名稱.title(圖表標題)
套件名稱.xlabel(x𠩜標標題)
套件名稱.ylabel(y𠩜標標題)
```

- 設計者可以自行設定 x 及 y 坐標範圍，語法為：

```python
套件名稱.xlim(起始值, 終止值)
套件名稱.ylim(起始值, 終止值)
```

[02_plot2.py][02_plot2.py]

---

### Matplotlib 顯示中文

- Matplotlib 預設無法顯示中文，所以前一範例中各種標題及圖例都使用英文，若要在 Matplotlib 顯示中文，在程式碼中加入這行即可。
`plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']`

- 為了能正常顯示負號，請再加入這行。
`plt.rcParams['axes.unicode_minus']=False`

---

### 柱狀圖

柱狀圖 是以 bar 方法繪製，語法為：

`套件名稱.bar(x座標串列, y座標串列, 其它參數...)`

[03_bar.py][03_bar.py]

---

### 圓餅圖

圓餅圖 是以 pie 方法繪製，語法為：

`套件名稱.pie(資料串列, 選擇性參數串列)`

- 「資料串列」是一個數值串列，為畫圓餅圖的資料，其為必要參數。
- 「選擇性參數串列」可有可無，參數名稱及功能為：
  - labels：每一個項目標題組成的串列。
  - colors：每一個項目顏色組成的串列。
  - explode：每一個項目凸出數值組成的串列，「0」表示正常顯示未爆出。
  - labeldistance：項目標題與圓心的距離是半徑的多少倍，例如「1.1」表示項目標題與圓心的距離是半徑的 1.1 倍。
  - autopct：項目百分比的格式，語法為「% 格式 %%」，例如「%2.1f%%」表示整數 2 位數，小數 1 位數。
  - shadow：布林值，True 表示圖形有陰影，False 表示圖形沒有陰影。
  - startangle：開始繪圖的起始角度，繪圖會以逆時針旋轉計算角度。
  - pctdistance：百分比文字與圓心的距離是半徑的多少倍。

---

[04_pie.py][04_pie.py]

[05_death_valley.py][05_death_valley.py]

---

[01_plot1.py]: /sample_codes/part6/01_plot1.py
[02_plot2.py]: /sample_codes/part6/02_plot2.py
[03_bar.py]: /sample_codes/part6/03_bar.py
[04_pie.py]: /sample_codes/part6/04_pie.py
[05_death_valley.py]: /sample_codes/part6/05_death_valley.py
