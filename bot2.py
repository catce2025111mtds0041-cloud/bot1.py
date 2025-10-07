import pyautogui
import time

#uma pausa entra os comando de 1segundo
pyautogui.PAUSE = 1
#clicar emuma tecla
pyautogui.press("win")
#escreve alguma coisa
pyautogui.write("chrome")

pyautogui.press("enter")

time.sleep(3)
pyautogui.write("youtube")

pyautogui.press("enter")

time.sleep(3)

pyautogui.click(x=225, y=462)

time.spleep(3)
pyautogui.click(x=1064, y=407)