#!usr/bin/env python
#-*- coding:utf-8 _*-

"""
@author:T-guoh
@file: server_monitor.py
@time: 2019/03/18
"""

import psutil
import os
import socket

cpu = {'user':0,'system':0,'idle':0,'percent':0}
mem = {'total' : 0, 'avaiable' : 0, 'percent' : 0, 'used' : 0, 'free' : 0}
disk_id = []
disk_total = []
disk_used = []
disk_free = []
disk_percent = []

#获取CPU信息
def get_cpu_info():
    cpu_times = psutil.cpu_times()
    cpu['user'] = cpu_times.user
    cpu['system'] = cpu_times.system
    cpu['idle'] = cpu_times.idle
    cpu['percent'] = psutil.cpu_percent(interval=2)

#获取Memory信息
def get_mem_info():
    mem_info = psutil.virtual_memory()
    mem['total'] = mem_info.total
    mem['avaiable'] = mem_info.available
    mem['percent'] = mem_info.percent
    mem['used'] = mem_info.percent
    mem['free'] = mem_info.free
#获取Disk信息
def get_disk_info():
    for id in psutil.disk_partitions():
        if 'cdrom' in id.opts or id.fstype == '':
            continue
        disk_name = id.device.split(':')
        s = disk_name[0]
        disk_id.append(s)
        disk_info = psutil.disk_usage(id.device)
        disk_total.append(disk_info.total)
        disk_used.append(disk_info.used)
        disk_percent.append(disk_info.percent)
        disk_free.append(disk_info.free)
#定义主函数
def main():
    get_cpu_info()
    cpu_status = cpu['percent']
    get_mem_info()
    mem_status = mem['percent']
    hostname = os.environ['COMPUTERNAME']
    username = os.environ['USERNAME']
    ip_addr = socket.gethostbyname(hostname)
    print('======基本信息======')
    print('主机名：'+ hostname+ '\nIP地址：' + ip_addr + '\n用户名：' + username)
    print('====================')
    print('\n=====资源使用率=====')
    print('CPU使用率：%s %%' % cpu_status)
    print('Mem使用率：%s %%' % mem_status)
    get_disk_info()
    for i in range(len(disk_id)):
        print('%s盘空闲率：%s %%' % (disk_id[i], round(100 - disk_percent[i], 2)))
    print('====================')
    os.system('pause')

if __name__ == '__main__':
    main()