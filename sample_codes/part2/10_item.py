dict1={"金牌":26,"銀牌":34,"銅牌":30}
items=list(dict1.items())
for name,num in items:
    print(f"得到的{name}數目為{num}面")
