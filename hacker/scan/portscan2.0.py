#!/usr/bin/env python
# -*- coding:utf-8 -*-
from socket import *
import threading
'''
    升级版，实现端口扫描的功能并使用多线程
    1.通过socket模块,判断是否连接成功
    2.连接成功即为该端口开放，否则为关闭
    3.加入threading模块，大幅提高扫面速度
    缺点：ip为固定
'''
lock = threading.Lock()
openNum = 0
threads = []

def portscan(host,port):
    global openNum
    try:
        s = socket(AF_INET,SOCK_STREAM)
        s.connect((host,port))
        lock.acquire()
        openNum+=1
        print('[+] %d open ' % port)
        lock.release()
        s.close()
    except:
        pass

def main():
    setdefaulttimeout(1)
    for p in range(1,1025):
        t = threading.Thread(target=portscan,args=('192.168.1.188',p))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print('[*] The scan is complete!')
    print('[*] A total of %d open port' % (openNum))

if __name__ == '__main__':
    main()