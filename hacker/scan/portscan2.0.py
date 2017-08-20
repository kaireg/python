#!/usr/bin/env python
# -*- coding:utf-8 -*-
from socket import *
import threading

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