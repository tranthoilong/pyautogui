import time
import pyautogui as sent

number = 10

time.sleep(5)

for i in range(number):

    if i>4:
        text="Lamf nguoifw yeue anh nha >_< <3 "
    else:
        text=f"{i+1}. Anh yeeu em <3"
    
    if i>7:
        text="Nha nha....!!!!! >_< "


    sent.typewrite(text,interval=0.1)

    sent.press("Enter")

    time.sleep(1)


