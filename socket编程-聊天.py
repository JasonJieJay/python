
============================================================================================
#server.py#
#coding=utf-8
import socket   #导入socket模块
import threading
ip_port = ('127.0.0.1',9999)    #以元组形式定一个IP和端口
sk = socket.socket()    #创建对象并且进行绑定IP进行监听
sk.bind(ip_port)
sk.listen(5)    #开始监听传入链接(可以挂起最大连接数)
def handle_sock(conn,addr):
        while True:
#        print('server online!!!')
#       conn,addr = sk.accept()        #conn代表客户端和服务端建立连接的通信链路
                client_date = conn.recv(1024).decode()        #acccept代表阻塞方式，没有收到请求就不会向下执行
                print(client_date)        #回复消息
                SR=input('Please input:')
                conn.sendall(('%s'%SR).encode())
                conn.close()
while True:
        conn,addr=sk.accept()

client_thread = threading.Thread(target=handle_sock,args=(conn,addr))
client_thread.start()
===========================================================================================
#client.py#
#coding=utf-8
import socket
ip_port = ('127.0.0.1',9999)
#sk = socket.socket()
#sk.connect(ip_port)
while True:
        sk = socket.socket()
        sk.connect(ip_port)
#       while True:
        SR=input('Please input:')
        sk.sendall(('%s'%SR).encode())
        ser_reply = sk.recv(1024).decode('utf8')
        print(ser_reply)
        sk.close()
====================================================================================================
 0211/0226-01.socket编程

学习目标
掌握scoket编程基本方法

课程内容
a.socket定义
b.socket对象
c.socket编程思路
d.开发实例


a.socket定义
套接字，用于描述IP、端口等，通过链路句柄，应用程序通过套接字向网络中发送除请求或者响应
socket遵循"一切皆为文件"思想，可以打开，读取，关闭
socket和file区别
file模块是针对指定文件进行打开，读写，关闭
socket模块是针对服务器和客户端socket进行打开，读写，关闭

b.socket对象
sk=socket.socket(socket.AT_INET,socket.socket_stream,0)
参数1：地址簇(IPV4,IPV6)
参数2：协议簇(tcp/udp)

c.socket编程思路
c1.tcp服务端
	1.创建爱呢套接字，绑定套接字到本地IP和端口
	2.开始监听连接
	3.进入循环，不断接受客户端连接请求
	4.接受传来的数据，并且发送数据给对方
	5.传输完毕，关闭套接字
c2.tcp客户端
	1.创建套接字，连接远程地址
	2.连接后发送数据和接收数据
	3.传输完毕关闭套接字


d.开发实例
server.py:
import socket
#导入socket模块
ip_port=('127.0.0.1',9999)
#以元组形式定一个IP和端口
sk=socket.socket()
#创建对象并且进行绑定IP进行监听
sk.bind(ip_port)
#开始监听传入链接(可以挂起最大连接数)
sk.listen(5)
while True:
        print('welcome to my server!!!')
        #conn代表客户端和服务端建立连接的通信链路
        conn,addr=sk.accept()
        #acccept代表阻塞方式，没有收到请求就不会向下执行
        client_date=conn.recv(1024)
        print(client_date)
        #回复消息
        conn.sendall(('server recieved your msg!').encode())
        conn.close()
client.py
import socket
ip_port=('127.0.0.1',9999)
sk=socket.socket()
sk.connect(ip_port)
sk.sendall(('im client!').encode())
ser_reply=sk.recv(1024)
print(ser_reply)
sk.close()
=====================================================================================================
0226-02.线程和进程
学习目标
掌握进程和线程的基本概念和应用方法

课程内容
a.进程和线程
b.多线程

a.进程和线程
进程：正在运行的程序实例
线程：进程的一个实体，被系统地理调度分配的基本单位，线程自己不拥有资源，
他可以和同属一个进程的线程共享资源

进程和线程的区别
1.地址空间：进程内的一个指定单元，进程至少有一个线程，共享进程的地址空间
，进程是有自己独立空间
2.资源拥有：进程的资源分配独立，统一进程内线程共享进程资源
3.线程是处理器调度的基本单位，进程不是
4.二者都可以并发执行

b.多线程
加速程序及计算的有效方式
b1.添加线程
import threading
print(threading.active_count())         #获取当前线程数量
print(threading.current_thread())       #查看当前运行的线程

#添加线程
def thread_job():
        print('当前线程是%s'%threading.current_thread())

def thread_job2():
        print('当前线程是%s'%threading.current_thread())

thread=threading.Thread(target=thread_job)
thread1=threading.Thread(target=thread_job2)
thread.start()
thread1.start()

b2.join功能
如果不加join功能，程序输出可能会混乱名，执行完全取决于执行的速度
import time
import threading
def t1():
        print('T1开始了')
        for i in range(10):
                time.sleep(0.1)
        print('T1结束')

def t2():
        print('t2开始了')
        print('t2结束了')

th1=threading.Thread(target=t1)
th2=threading.Thread(target=t2)
th1.start()
th2.start()
th2.join()
th1.join()
print('finished')


b3.gil
python完全支持多线程编程，但是代码并行是不安全的，通常会有个全局解释器进行控制，确保任何时候只有一个线程在执行

b4.线程锁
lock在不同线程中共享同一个内存时候，相互之间不影响，使用lock方法实在每个线程执行运行修改之前，执行lock.acquire()将内存上锁
def job1():
 42         global A,lock
 43         lock.acquire()
 44         for i in range(10):
 45                 A+=1
 46                 print('job',A)
 47         lock.release()
 48 
 49 def job2():
 50         global A,lock
 51         lock.acquire()
 52         for i in range(10):
 53                 A+=10
 54                 print('job2',A)
 55         lock.release()
 56 
 57 lock=threading.Lock()
 58 A=0
 59 th1=threading.Thread(target=job1)
 60 th2=threading.Thread(target=job2)
 61 th1.start()
 62 th2.start()
 63 th2.join()
 64 th1.join()
=======================================================================================
 0211/例子-0226-01.多线程.py
#coding=utf-8
import time
import threading
'''
import threading
print(threading.active_count())		#获取当前线程数量
print(threading.current_thread())	#查看当前运行的线程
#添加线程
def thread_job():
	print('当前线程是%s'%threading.current_thread())
def thread_job2():
	print('当前线程是%s'%threading.current_thread())
thread=threading.Thread(target=thread_job)
thread1=threading.Thread(target=thread_job2)
thread.start()
thread1.start()
'''
'''
def t1():
	print('T1开始了')
	for i in range(10):
		time.sleep(0.1)
	print('T1结束')
def t2():
	print('t2开始了')
	print('t2结束了')
th1=threading.Thread(target=t1)
th2=threading.Thread(target=t2)
th1.start()
th2.start()
th2.join()
th1.join()
print('finished')
'''
def job1():
	global A,lock
	lock.acquire()
	for i in range(10):
		A+=1
		print('job',A)
	lock.release()

def job2():
	global A,lock
	lock.acquire()
	for i in range(10):
		A+=10
		print('job2',A)
	lock.release()

lock=threading.Lock()
A=0
th1=threading.Thread(target=job1)
th2=threading.Thread(target=job2)
th1.start()
th2.start()
th2.join()
th1.join()







