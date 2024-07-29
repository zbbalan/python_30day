import socket
if __name__ == '__main__':
    #窗机tcp套接字
    tcp_agent_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      # 设置端口号复用，让程序退出端口号立即释放
    tcp_agent_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
     # 给程序绑定端口号
    tcp_agent_socket.bind(('', 7788))
    # 设置监听
    # 128:最大等待建立连接的个数， 提示： 目前是单任务的服务端，同一时刻只能服务与一个客户端，后续使用多任务能够让服务端同时服务与多个客户端，
    # 不需要让客户端进行等待建立连接
    # listen后的这个套接字只负责接收客户端连接请求，不能收发消息，收发消息使用返回的这个新套接字来完成
    tcp_agent_socket.listen(128)
     # 等待客户端建立连接的请求, 只有客户端和服务端建立连接成功代码才会解阻塞，代码才能继续往下执行
    # 1. 专门和客户端通信的套接字： service_client_socket
    # 2. 客户端的ip地址和端口号： ip_port
    service_client_socket,ip_port = tcp_agent_socket.accept()
     # 代码执行到此说明连接建立成功
    print("客户端ip和端口号",ip_port)
     # 接收客户端发送的数据, 这次接收数据的最大字节数是1024
    recv_data=service_client_socket.recv(1024)
      # 获取数据的长度
    recv_data_length=len(recv_data)
    print("数据长度为",recv_data_length)
     # 对二进制数据进行解码
    recv_content=recv_data.decode("utf-8")
    print("接收客户端数据",recv_content)
     # 准备发送的数据
    send_data="问题处理中".encode("utf-8")
     # 发送数据给客户端
    service_client_socket.send(send_data)
    # 关闭服务与客户端的套接字， 终止和客户端通信的服务
    tcp_agent_socket.close()


