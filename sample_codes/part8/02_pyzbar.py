import cv2
import pyzbar.pyzbar as pyzbar

img=cv2.imread("test.jpg")
decodeObjects=pyzbar.decode(img)
for obj in decodeObjects:
    print(obj.data)

# 如果程式執行有錯，請安裝vcredist_x64.exe試試
