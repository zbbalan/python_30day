import socket
if __name__ == '__main__':
    # 创建tcp客户端套接字
    # 1. AF_INET：表示ipv4
    # 2. SOCK_STREAM: tcp传输协议
    tcp_client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
     # 和服务端应用程序建立连接
    tcp_client_socket.connect(('127.0.0.1',7788))
     # 代码执行到此，说明连接建立成功
    # 准备发送的数据
    send_data="给agent发送数据".encode("utf-8")
     # 发送数据
    tcp_client_socket.send(send_data)
    # 接收数据, 这次接收的数据最大字节数是1024
    recv_data=tcp_client_socket.recv(1024)
     # 返回的直接是服务端程序发送的二进制数据
    print(recv_data)
      # 对数据进行解码
    recv_conter=recv_data.decode("utf-8")
    print("接收服务端的数据为",recv_data)
    tcp_client_socket.close()
    #关闭套接字
    print("客户端退出")