import jieba

contents="今天天氣很不錯"
#contents="今年中秋節前夕，藝人甄珍在高雄市新聞局長王淺秋陪同下，到高雄市鳳山早療中心，用真誠、溫暖的關懷，親切陪伴孩子，舉手投足流露大明星的風範，卻沒有明星的架子，是高雄一陣溫暖的微風"
#contents=open("citymoon.txt",encoding="utf-8").read()
#jieba.set_dictionary("dict.txt")
words=jieba.cut(contents,cut_all=False)
for word in words:
    print(word,end="/")
