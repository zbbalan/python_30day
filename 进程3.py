import multiprocessing
import time
import os



def task():
    for i in range(10):
        print("任务执行中。。。。。")
        time.sleep(2)

if __name__ == '__main__':
    sub_process = multiprocessing.Process(target=task)
    sub_process.daemon = True
    sub_process.start()
    print("子进程pid：", sub_process.pid)
    time.sleep(1)
    print("over")
    sub_process.terminate()
    exit(0)