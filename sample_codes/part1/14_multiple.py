a=int(input("請輸入 a 的值："))
b=int(input("請輸入 b 的值："))
maxno=a*b+1
for i in range(1,maxno):
    if(i%a==0 and i%b==0):
        print(f"{a} 和 {b} 的最小公倍數 = {i}")
        break
  