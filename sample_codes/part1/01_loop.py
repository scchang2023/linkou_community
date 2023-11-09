total = 0

def show(n):
    print("第 " + str(n) + " 次執行迴圈")
    
for i in range(1,11):
    show(i)
    total = total + i
print("1+2+...+10 = " + str(total))