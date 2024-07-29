import threading
import time

def show_info():
    for i in range(5):
        print("test:",i)
        time.sleep(1)

if __name__ == '__main__':
    t = threading.Thread(target=show_info,daemon=True)
    t.start()
    time.sleep(2)
    print("over")
