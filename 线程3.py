import threading
import time
log_list = 0
def info_show():
    for i in range(10000):
        global log_list
        log_list += 1
        #time.sleep(0.2)
        
    print(log_list)

def inif_show():
    for i in range(10000):
        global log_list
        log_list += 1
        #time.sleep(1)
    print(log_list)

if __name__ == '__main__':
    t1 = threading.Thread(target=info_show)
    t2 = threading.Thread(target=inif_show)
    t1.start()          ###线程之间共享变量好处是可以对全局变量的数据进行共享
    t1.join()           ##线程之间共享全局变量可能会导致数据出现错误问题，可以使用线程同步方式来解决这个问题。线程等待(join)
    t2.start()