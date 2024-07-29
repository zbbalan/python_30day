import threading
import time
""""使用互斥锁的时候需要注意死锁的问题，要在合适的地方注意释放锁。
死锁一旦产生就会造成应用程序的停止响应，应用程序无法再继续往下执行了
"""

lock = threading.Lock()  ###创建全局锁

def get_value(index):
    lock.acquire() ##上锁
    print(threading.current_thread())
    my_list = [1,2,3,4,5,6,7,8,9,10]
    
    if index >= len(my_list):
        print("下标越界",index)
        lock.release()  ###在下标越界的地方添加释放锁，让后面也能获取到值，
        return
    value = my_list[index]
    print(value)
    time.sleep(1)
    lock.release() ##释放锁
 
if __name__ == '__main__':
    for i in range(30):     ###模拟大量操作
        t = threading.Thread(target=get_value,args=(i,))
        t.start()

    