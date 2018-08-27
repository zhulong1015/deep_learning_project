'''
TCP客户端的创建和运行
'''
import socket
# 初始化Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 连接目标的ip和端口
s.connect(('127.0.0.1', 9999))
while True:
    # 接收消息
    print('服务器：' + s.recv(1024).decode('utf-8'))
    # 发送消息
    print('请输入客户端想对服务器说的话：')
    str_text = input()
    s.send(str_text.encode('utf-8'))
    # print('服务器说：' + s.recv(1024).decode('utf-8'))
    # print('请输入想对服务器说的话')
    # str = input()
    # s.send(str.encode('utf-8'))
# 关闭套接字
s.close()