dict1={"趙一哥":85, "錢二姊":93, "孫三弟":67}
name=input("輸入學生姓名：")
if name in dict1:  
    print(f"{name}的成績為{dict1[name]}")
else:  
    score=int(input("輸入學生分數："))
    dict1[name]=score
    print(f"字典內容：{dict1}")