#!/usr/bin/env python
# -*- coding:utf-8 -*-

from socket import *
import threading
import argparse
'''
    最终版，实现端口扫描的功能并使用多线程，同时可以实现多个ip扫描
    1.通过socket模块,判断是否连接成功
    2.连接成功即为该端口开放，否则为关闭
    3.加入threading模块，大幅提高扫面速度
    4.加入argpares，可以添加参数加入多个IP地址
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
        print('[+] %d open' % port)
        lock.release()
        s.close()
    except:
        pass

def main():
    p = argparse.ArgumentParser(description='Port scanner!')
    p.add_argument('-H', dest='hosts', type=str)
    args = p.parse_args()
    hostList = args.hosts.split(',')
    setdefaulttimeout(1)
    for host in hostList:
        print('Scanning the host:%s......' % (host))
        for p in range(1, 65537):
            t = threading.Thread(target=portscan, args=(host, p))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

        print('[*] The host:%s scan is complete!' % (host))
        print('[*] A total of %d open port ' % (openNum))

if __name__ == '__main__':
    main()