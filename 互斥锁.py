import threading
import time
##通过执行结果可以地址互斥锁能够保证多个线程访问共享数据不会出现数据错误问题
'''互斥锁的作用就是保证同一时刻只能有一个线程去操作共享数据，保证共享数据不会出现错误问题
使用互斥锁的好处确保某段关键代码只能由一个线程从头到尾完整地去执行
使用互斥锁会影响代码的执行效率，多任务改成了单任务执行
互斥锁如果没有使用好容易出现死锁的情况
'''

g_num = 0
lock = threading.Lock()  ###创建全局互斥锁
def test1():
    lock.acquire()  ###获取锁
    for i in range(1000000):
        global g_num
        g_num += 1
    print("test1 g_num = %d" % g_num)
    lock.release()   ###释放锁
def test2():
    lock.acquire()
    for i in range(1000000):
        global g_num
        g_num += 1
    print("test2 g_num = %d" % g_num)
    lock.release()

if __name__ == "__main__":
    t1 = threading.Thread(target=test1)
    t2 = threading.Thread(target=test2)
    t1.start()
    t2.start()