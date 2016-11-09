#coding:utf8
import os
import subprocess
import win32gui
import time
import win32api,win32con

l=['~','!','@','#','$','%','^','&','*','(',')','_','+','{','}',':','"','|','<','>','?']
def putKeyBoard(str):
    for i in str:
        if i.isdigit():
            win32api.keybd_event(ord(i),0,0,0)
            win32api.keybd_event(ord(i),0,win32con.KEYEVENTF_KEYUP,0)
        elif i.isalpha() and i==i.lower():
            win32api.keybd_event(ord(i.upper()),0,0,0)
            win32api.keybd_event(ord(i.upper()),0,win32con.KEYEVENTF_KEYUP,0)
        elif i.isalpha() and i==i.upper():
            win32api.keybd_event(20,0,0,0)#Caps Lock
            win32api.keybd_event(20,0,win32con.KEYEVENTF_KEYUP,0)
            win32api.keybd_event(ord(i),0,0,0)
            win32api.keybd_event(ord(i),0,win32con.KEYEVENTF_KEYUP,0)
            win32api.keybd_event(20,0,0,0)#Caps Lock
            win32api.keybd_event(20,0,win32con.KEYEVENTF_KEYUP,0)
        else:
            pass
            print '是特殊字符，跳过'
        #特殊字符在win32con中判断，暂时只识别出来+,-,/,
        # elif i in l:
            # win32api.keybd_event(ord(i),0,0,0)
            # win32api.keybd_event(ord(i),0,win32con.KEYEVENTF_KEYUP,0)
            # win32api.keybd_event(win32con.VK_SHIFT,win32api.MapVirtualK5ey(win32con.VK_SHIFT,0),0,0)#shift
            # win32api.keybd_event(134,0,0,0)
            # win32api.keybd_event(134,0,win32con.KEYEVENTF_KEYUP,0)
            # win32api.keybd_event(win32con.VK_SHIFT,win32api.MapVirtualKey(win32con.VK_SHIFT,0),win32con.KEYEVENTF_KEYUP,0)
        # else:
        #     print i,ord(i)
        #     win32api.keybd_event(135,0,0,0)
        #     win32api.keybd_event(135,0,win32con.KEYEVENTF_KEYUP,0)
        time.sleep(0.5)

if __name__=='__main__':
    subprocess.Popen('D:\Program Files (x86)\Tencent\QQ\Bin\QQScLauncher.exe')
    time.sleep(2)
    hlg = win32gui.FindWindow(None,'QQ')
    (left,top,right,bottom) = win32gui.GetWindowRect(hlg)
    win32api.SetCursorPos((left+280,top+268))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

    login_name ='123456789'
    passoword = '123asdfYdn'

    putKeyBoard(login_name)
    win32api.keybd_event(13,0,0,0)#enter 换行
    win32api.keybd_event(13,0,win32con.KEYEVENTF_KEYUP,0)
    putKeyBoard(passoword)
    win32api.keybd_event(13,0,0,0)
    win32api.keybd_event(13,0,win32con.KEYEVENTF_KEYUP,0)
