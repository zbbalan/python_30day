import socket
import threading
import time

# 处理客户端的请求操作
def handle_client_request(server_client_socket,ip_port):
    #循环接收客户端发送的信息
    while True:
        #接收客户端发送的信息
        recv_data = server_client_socket.recv(1024)
        if recv_data:
            print("客户端%s说:%s"%(ip_port,recv_data.decode("utf-8")))
            server_client_socket.send("服务器已收到".encode("utf-8"))
            time.sleep(1)
        else:
            print("客户端%s退出聊天室"%ip_port)
            break
    server_client_socket.close()

if __name__ == "__main__":
    #创建套接字
    tcp_server_sorcket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #设置端口号复用
    tcp_server_sorcket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)
    #绑定端口号
    tcp_server_sorcket.bind(("",7788))
    #设置监听
    tcp_server_sorcket.listen(128)
    ##循环等待客户端连接
    while True:
        service_client_socket,ip_port = tcp_server_sorcket.accept()
        print("客户端连接成功",ip_port)
        # 当客户端和服务端建立连接成功以后，需要创建一个子线程，不同子线程负责接收不同客户端的消息
        sub_thread = threading.Thread(target=handle_client_request,args=(service_client_socket,ip_port))
        #设置守护进程
        sub_thread.setDaemon(True)
        #启动子进程
        sub_thread.start()
        
