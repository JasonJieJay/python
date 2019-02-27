
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
