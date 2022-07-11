import pyperclip
import pyautogui
import time

while True:
        with open('password.txt','r', encoding='UTF-8') as file:    #password文件同目录下
            #一句话一行
            lst = file.readlines()
            length=len(lst)
            #print(len(lst))
            time.sleep(5)
            for i in range(length):
                #print(type(lst), lst[i])
                pyperclip.copy(lst[i])
                #pyperclip.paste()
                pyautogui.hotkey('ctrl','v')
                time.sleep(1)
                #这是控制聊天的频率
                #如果有的游戏如果聊天过快会被禁言，那么调高频率间隔即可
                pyautogui.hotkey('enter')