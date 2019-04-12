#!/usr/bin/env python
# encoding: utf-8
"""
@version: python3.5
@author: wolf_dreams
@contact: gh1578@qq.com
@2019-3-25-day03: login.py
@time: 2019/3/23 18:54
"""
import sys
count = 0
flag = True
while flag:
    username = input("Enter user name:")
    if username == 'wolf_dreams':
        password = input("Enter password:")
        if password == '123456':
            print("welcome to my python websit!!!")
            sys.exit()
        else:
            print("Enter password error,please again!")
            count += 1
            if count == 3:
                print("The number of input has been %s,and the account is locked!" % count)
                print("Please try again in five minutes!")
                sys.exit()
            continue
    else:
        print("Enter user name error,please again!")
        count += 1
        if count == 3:
            print("The number of input has been %s,and the account is locked!" % count)
            print("Please try again in five minutes!")
            sys.exit()
        continue

