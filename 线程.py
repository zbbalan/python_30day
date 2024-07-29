import threading   ##导入线程包
import time
def sing(): ###创建任务
    for i in range(5):
        print('唱')
        time.sleep(3)

def tanks(count):
    for i in range(count):
        print('坦克')
        time.sleep(3)



def sance():
    for i in range(5):
        print('跳')
        time.sleep(3)

def dances(like):
    for i in range(like):
        print('幸运')
        time.sleep(3)


if __name__ == '__main__':
    t1 = threading.Thread(target=sing)  ##创建子线程并执行任务
    t2 = threading.Thread(target=sance)
    t3 = threading.Thread(target=tanks,args=(5,)) #args 表示以元组的方式给执行任务传参
    t4 = threading.Thread(target=dances,kwargs={'like':5}) #kwargs 表示以字典的方式给执行任务传参
    t1.start()
    t2.start()  ##启动子线程 
    t3.start()
    t4.start()
