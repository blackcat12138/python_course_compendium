'''
    线程同步：一个一个线程的完成,一个做完另一个才能进来。
             这样能够保证的数据安全性,但相对的效率将会降低。
    多线程的优点在于可以同时运行多个任务(感觉是这样),
    但当线程需要共享数据时,可能存在数据不同步的问题。
    为了避免这种情况发生,引入了锁。

    结论:
        由于在python解释器中有Gil锁,在数据量小的情况下,
        并没有出现数据不同步的现象,即使加入lock锁也是一样的,
        但在数据量大的情况下,就必须加lock锁实现数据同步。
'''

import threading
import random
import time

lock = threading.Lock()
lists = [0] * 10


# print(lists)

def task1():
    # 获取线程锁,若已经上锁,则等待锁的释放
    lock.acquire()  # 阻塞
    for i in range(len(lists)):
        lists[i] = 1
        time.sleep(0.5)
    lock.release()  # 释放锁


def task2():
    lock.acquire()  # 阻塞
    for i in range(len(lists)):
        print('--------->', i)
        time.sleep(0.5)
    lock.release()  # 释放锁


if __name__ == '__main__':
    t1 = threading.Thread(target=task1)
    t2 = threading.Thread(target=task2)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print(lists)