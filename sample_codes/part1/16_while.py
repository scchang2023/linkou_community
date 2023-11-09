total=i=1
n=int(input("請輸入正整數 n 的值："))
while(i<=n):
    total*=i  
    i+=1      
print(f"{n}!={total}")