from gtts import gTTS
import os

str1="今天天氣很好"
# str1="【原醉酒餐館】位於熱鬧的花蓮市區，於建國路的一處轉角，店面外觀在白天看似平凡，但到了夜晚店內的燈光便會轉化為昏黃浪漫的微醺氣氛，加上店內花草與蠟燭的特色擺飾，映襯紅磚牆彷如來到巴黎夜晚街道上的街邊小餐館用餐一樣。"
tts=gTTS(str1,lang="zh-tw")
tts.save('gtts.mp3')
os.system("gtts.mp3")

# import speech_recognition
# import pyaudio

# r=speech_recognition.Recognizer()
# with speech_recognition.Microphone() as source: 
#     print("請開始說話:")       
#     audio=r.listen(source)
# Text=r.recognize_google(audio,language="zh-TW")   
# print(Text)
