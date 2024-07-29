import multiprocessing
import time
import os

def tesk(count):### 带有参数的任务
    for i in range(count):
        print("##" *10)
        time.sleep(1)
    else:
        print("任务执行完毕")

def tank(classA):
    for i in range(classA):
        print("任务等待XXX" * 5)
    else:
        print("任务等待中")

if __name__ == '__main__':
    sub_process = multiprocessing.Process(target=tesk,args=(5,)) #args 表示以元组的方式给执行任务传参
    cub_process = multiprocessing.Process(target=tank,kwargs={"classA": 5}) #kwargs 表示以字典方式给执行任务传参
    sub_process.start()
    cub_process.start()
