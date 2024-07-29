import multiprocessing   ###导入进程包
import time
import os

##绘制进程函数
def dance():
    for i in range(5):
        print("唱")
        time.sleep(0.5)

def sing():
    for i in range(5):
        print("跳")
        time.sleep(0.5)

def rap():
    for i in range(5):
        print("rap")
        time.sleep(0.5)

'''##创建进程对象##创建进程
if __name__ == '__main__':
    dance_process = multiprocessing.Process(target=dance,name="myprocess")
    sing_process = multiprocessing.Process(target=sing,name="myprocess1")
    rap_process = multiprocessing.Process(target=rap,name="myprocess2")

####启动进程
    dance_process.start()
    sing_process.start()
    rap_process.start()'''


def dance1():
    print("进程🆔：",os.getpid())###获取进程pid
    print("父进程🆔：",os.getppid())##获取父id
    print("dance",multiprocessing.current_process()) ###获取进程对象
    for i in range(5):
        print("唱")
        time.sleep(1)
def sing1():
    print("进程🆔：",os.getpid())
    print("父进程🆔：",os.getppid())##获取父id
    print("dance",multiprocessing.current_process()) ###获取进程对象
    for i in range(5):
        print("跳")
        time.sleep(1)
def rap1():
    print("进程🆔：",os.getpid())
    print("父进程🆔：",os.getppid())##获取父id
    print("dance",multiprocessing.current_process()) ###获取进程对象
    for i in range(5):
        print("rap")
        time.sleep(1)

##创建进程对象##创建进程
if __name__ == "__main__":
    print("main",os.getpid())
    print("main",multiprocessing.current_process())
    dance1_process = multiprocessing.Process(target=dance1,name="myprocess1")
    sing1_process = multiprocessing.Process(target=sing1,name="myprocess2")
    rap1_process = multiprocessing.Process(target=rap1,name="myprocess3")
    dance_process = multiprocessing.Process(target=dance,name="myprocess")
    sing_process = multiprocessing.Process(target=sing,name="myprocess1")
    rap_process = multiprocessing.Process(target=rap,name="myprocess2")

    dance1_process.start()
    sing1_process.start()
    rap1_process.start()
    ####启动进程
    dance_process.start()
    sing_process.start()
    rap_process.start()

