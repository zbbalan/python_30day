import socket
import unittest
from unittest.mock import MagicMock
from your_module import handle_client_request  # Replace 'your_module' with the actual module name where handle_client_request is located

class TestHandleClientRequest(unittest.TestCase):
    def setUp(self):
        # 创建一个模拟的socket对象
        self.mock_socket = MagicMock(spec=socket.socket)
        # 设置ip_port参数
        self.ip_port = ('127.0.0.1', 7788)

    def test_handle_client_request_normal(self):
        # 模拟客户端发送数据
        self.mock_socket.recv.return_value = b'Hello, Server!'
        
        # 调用待测函数
        handle_client_request(self.mock_socket, self.ip_port)
        
        # 验证socket是否发送了正确的响应
        self.mock_socket.send.assert_called_once_with(b"服务器已收到")
        # 验证socket是否关闭
        self.mock_socket.close.assert_called_once()

    def test_handle_client_request_no_data(self):
        # 模拟客户端不发送数据
        self.mock_socket.recv.return_value = b''
        
        # 调用待测函数
        handle_client_request(self.mock_socket, self.ip_port)
        
        # 验证socket是否关闭
        self.mock_socket.close.assert_called_once()

if __name__ == '__main__':
    unittest.main()