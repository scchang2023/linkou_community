import matplotlib.pyplot as plt
import jieba
from wordcloud import WordCloud

contents=open("citymoon.txt",encoding="utf-8").read()
jieba.set_dictionary("dict.txt")
words=jieba.cut(contents,cut_all=False)
word_space_split= " ".join(words)
wc=WordCloud(font_path="kaiu.ttf",background_color="white")
wc.generate(word_space_split)
plt.imshow(wc)
plt.axis("off")
plt.show()

# pip install wordcloud
# error: Microsoft Visual C++ 14.0 or greater is required. Get it with "Microsoft C++ Build Tools": https://visualstudio.microsoft.com/visual-cpp-build-tools/