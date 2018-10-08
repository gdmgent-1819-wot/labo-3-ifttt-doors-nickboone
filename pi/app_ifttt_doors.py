import requests
from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
from signal import pause

sense = SenseHat()

def pushed_up(event):
    if event.action == ACTION_RELEASED:
        r = requests.post("https://maker.ifttt.com/trigger/button_pressed/with/key/ms-PZR9LYe-KfY0-pZ-SoN3dNFMioRFHo0GH2Dw2ct_",
        data={ "value1" : "de voordeur is open!" })
    
def pushed_down(event):
    
    if event.action == ACTION_RELEASED:
        r = requests.post("https://maker.ifttt.com/trigger/button_pressed/with/key/ms-PZR9LYe-KfY0-pZ-SoN3dNFMioRFHo0GH2Dw2ct_",
        data={ "value1" : "de voordeur sluit!" })
    

def pushed_left(event):
    
    if event.action == ACTION_RELEASED:
        r = requests.post("https://maker.ifttt.com/trigger/button_pressed/with/key/ms-PZR9LYe-KfY0-pZ-SoN3dNFMioRFHo0GH2Dw2ct_",
        data={ "value1" : "de achterdeur is open!" })
    

def pushed_right(event):
    
    if event.action == ACTION_RELEASED:
        r = requests.post("https://maker.ifttt.com/trigger/button_pressed/with/key/ms-PZR9LYe-KfY0-pZ-SoN3dNFMioRFHo0GH2Dw2ct_",
        data={ "value1" : "de achterdeur sluit!" })


sense.stick.direction_up = pushed_up
sense.stick.direction_down = pushed_down
sense.stick.direction_left = pushed_left
sense.stick.direction_right = pushed_right
pause()


