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
limit_count = 3
retry_count = 0
account = 'account.txt'
account_lock = 'lock_account.txt'
while retry_count < limit_count:
    username = input('\033[32;1mEnter user name:\033[0m')
    with open(account_lock,'r') as lock:
        for line in lock.readlines():
            line = line.split()
            if username == line[0]:
                sys.exit('\033[31;1mThe %s account is locked.Please try again in five minutes!\033[0m' %username)
    password = input('\033[32;1mEnter password:\033[0m')
    with open(account,'r') as f:
        match_flag = False
        for line in f.readlines():
            user,passwd = line.strip('\n').split()
            if username == user and password == passwd:
                print('Match',username)
                match_flag = True
                break
        if match_flag == False:
            print('user unmatched!')
            retry_count += 1
        else:
            print("welcome to my python websit!!!")
            sys.exit()
else:
    print('\033[31;1mThe %s account is locked.Please try again in five minutes!\033[0m' %username)
    with open(account_lock,'a') as f:
        f.write(username + '\n')
