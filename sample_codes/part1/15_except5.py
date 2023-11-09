n=int(input("請輸入正整數："))
for i in range(1,n+1):
    if i%5 ==0:
        continue
    print(i,end=" ")