#!/usr/bin/env python
# -*- coding:utf-8 -*-
from socket import *
'''
    简单版，主要在实现端口扫描的功能
    1.通过socket模块,判断是否连接成功
    2.连接成功即为该端口开放，否则为关闭
    缺点：ip为固定，单线程速度较慢
'''

def portscan(host,port):
    try:
        s = socket(AF_INET,SOCK_STREAM)
        s.connect((host,port))
        print('[+] %d open' % port)
        s.close()
    except:
        print('[-] %d close' % port)

def main():
    setdefaulttimeout(1)
    for p in range(1,1025):
        portscan('192.168.1.188',p)

if __name__ == '__main__':
    main()