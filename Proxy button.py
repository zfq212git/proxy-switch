#!/usr/bin/env python3.6
#from selenium import webdriver

# PROXY = "23.23.23.23:3128" # IP:PORT or HOST:PORT

#chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--proxy-server=%s' % PROXY)

# chrome = webdriver.Chrome(chrome_options=chrome_options)
# chrome.get("http://baidu.com")

import os
#import Skype4Py

proxy="10.35.147.36"
port=8080

def Proxy_on():
    status = os.system('networksetup -setwebproxystate "Wi-Fi" on')
    if(status>0):
        print("let's exit this operation...")
    else:
        os.system('networksetup -setsecurewebproxystate "Wi-Fi" on')

def Proxy_off():
    status = os.system('networksetup -setwebproxystate "Wi-Fi" off')
    if(status>0):
        print("let's exit this operation...")
    else:
        os.system('networksetup -setsecurewebproxystate "Wi-Fi" off')


def Switch_proxy_status():
    status=os.system('networksetup -getsecurewebproxy "Wi-Fi" | grep "No"')

    if(status>0):
        print("turning proxy OFF....")
        Proxy_off()

    if(status==0):
        print("turning proxy ON....")
        Proxy_on()
    
Switch_proxy_status()
