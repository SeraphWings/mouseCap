import cv2
import numpy
import mss
import pyautogui

global mouseX
global mouseY
global mon
mouseX = 0
mouseY = 0
mon = {"top": mouseX, "left": mouseY, "width": 800, "height": 640}

def cursorXY(event, x, y, flags, param):
    global mouseX
    global mouseY

 
def screen_record_efficient():
    
    global mouseX
    global mouseY
    global mon

    title = "mouse capture"
    sct = mss.mss()
    img = numpy.asarray(sct.grab(mon))
    cv2.imshow(title, img)

    while True:
        mouseX, mouseY = pyautogui.position()
        mon["left"] =  int( mouseX - (mon["width"]/2) )
        mon["top"] =  int( mouseY - (mon["height"]/2) )

        img = numpy.asarray(sct.grab(mon))
        cv2.imshow(title, img)
        
        if cv2.waitKey(25) & 0xFF == ord("q"):
            break

        if cv2.getWindowProperty(title,cv2.WND_PROP_VISIBLE) < 1:        
            break

    cv2.destroyAllWindows()
    

screen_record_efficient()