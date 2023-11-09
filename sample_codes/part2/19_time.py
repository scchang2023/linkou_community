import time as t

print(t.time())
print(t.localtime())
print(f"現在是{t.localtime().tm_mon}月")
print(t.ctime())

