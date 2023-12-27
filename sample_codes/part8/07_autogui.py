import time
import pyautogui

sWidth,sHeight=pyautogui.size() 
print(sWidth,sHeight)

#找座標位置
time.sleep(10)
mouseX,mouseY=pyautogui.position()
print(mouseX,mouseY)

#點擊小畫家icon
#time.sleep(1)
#pyautogui.moveTo(1352,1174)
#pyautogui.click()

##小畫家畫四方型
#time.sleep(3)
#pyautogui.click(365,110)
#pyautogui.moveTo(400,400,duration=3) 
#pyautogui.dragRel(200,0, button='left', duration=3)
#pyautogui.dragRel(0, 200, duration=3, button='left')  
#pyautogui.dragRel(-200, 0, duration=3, button='left') 
#pyautogui.dragRel(0, -200, duration=3, button='left') 

#小畫家輸入文字
#pyautogui.click(431,118)
#time.sleep(1)
#pyautogui.doubleClick(420,500,button="left")
#time.sleep(1)
#pyautogui.press("shift")
#pyautogui.typewrite("hello world!")


