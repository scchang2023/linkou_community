scores=[]
total=inscore=0
while(inscore != -1):
    inscore=int(input("請輸入學生的成績："))
    if (inscore!=-1):  # 將成績加入 scores 串列中
        scores.append(inscore)
print(f"共有 {len(scores)} 位學生")
for score in scores:  # 將成績累加
    total+=score
average=total/(len(scores))  #求平均值
print(f"本班總成績：{total}分，平均成績：{average:5.2f}分")