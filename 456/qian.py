import win32gui,win32api,win32con,time
from win32api import GetSystemMetrics
from PIL import ImageGrab
def PilImage(x,y):
    a,b=GetSystemMetrics(0),GetSystemMetrics(1)
    im=ImageGrab.grab((0,0,a,b))
    pix=im.load()
    return pix[x,y]

def DisplaySize():
    return GetSystemMetrics(0),GetSystemMetrics(1)


def LeftClick(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0,)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0,)

def RightClick(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, x, y, 0, 0)


def PressOnce(x):
    win32api.keybd_event(x,0,0,0)


