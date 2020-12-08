#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 17:36:28 2020

@author: rahul
"""

import socket
import speedtest
import tkinter as tk


###end import libraries
window = tk.Tk()
window.title('IP Checker & Speed Tester')

frame = tk.Frame(window).pack()

speed = speedtest.Speedtest()
#userinput = tk.Entry(window, width 40)
user_input = input("Enter the web url for which you want to check the IP Address. If you wish to just test your internet connection, keep it blank by just pressing Enter Key : ")

def getIPAddress(user_input):
    if user_input == '' :
        ipaddress = socket.gethostbyname(socket.gethostbyname('www.google.com'))
        if ipaddress == '127.0.0.1':
            print("You are NOT connected to Internet at the moment")
        else:
            print("You are Connected to the internet.")
            user_input1 = input('Do you wish to test your internet speed? :')
            if user_input1 == 'y':
                print("Your download speed is : " + str(speed.download()))
                print("Your upload speed is : " + str(speed.upload()))
            else:
                print("thank you for using the ipchecker script!")
                
            
    else:
        ipaddress = socket.gethostbyname(socket.gethostbyname(user_input))
        if ipaddress == '127.0.0.1':
            print("You are NOT connected to Internet at the moment")
            
        else:
            print("You are connected to Internet! The IP Address for your website {} is {}" .format(user_input, ipaddress))
            
            user_input1 = input('Do you wish to test your internet speed? :')
            if user_input1 == 'y':
                print("Your download speed is : " + str(speed.download()))
                print("Your upload speed is : " + str(speed.upload()))
                
            else:
                print("Thank You for using the ipchecker script!")
            
            
getIPAddress(user_input)           
            
        
