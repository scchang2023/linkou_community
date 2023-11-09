scores=[]
while True:
    inscore=input("請輸入學生的成績：")
    if (inscore==""):
        break
    # 將成績轉為數值後加入 scores 串列中
    scores.append(int(inscore))  

scores2=sorted(scores,reverse=True) # 由大到小排序
print(f"成績由大到小排序：{scores2}") 