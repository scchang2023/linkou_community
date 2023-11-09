fruits=["香蕉","蘋果","橘子","鳳梨","西瓜"]
while True:
    print(f"串列元素有：{fruits}")
    fruit=input("請輸入要刪除的水果(Enter 結束)：")
    if (fruit==""):
        break
    n = fruits.count(fruit) 
    if (n>0):  # 串列元素存在
        fruits.remove(fruit)
    else:
        print(f"{fruit}不在串列中!")