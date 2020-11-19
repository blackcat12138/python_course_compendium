'''
    线程中的死锁
        死锁：两个线程分别占有一部分资源且同时等待对方的资源,将会造成死锁。
        死锁的产生：资源分配不当。
        解决：
            1.重构代码
            2.在acquire()函数中加入timeout参数
'''
import time
from threading import Thread, Lock

lockA = Lock()
lockB = Lock()


class MyThread(Thread):
    # def __init__(self):
    #     pass

    def run(self):  # start()
        # 若可以获取到锁则返回True
        if lockA.acquire():
            print(self.name + '获取A锁')  # 底层默认的名称
            time.sleep(0.1)
            if lockB.acquire(timeout=4):
                print(self.name + '获取B锁,原来还有A锁')
                lockB.release()
            lockA.release()


class MyThread1(Thread):
    def run(self):  # start()
        # 若可以获取到锁则返回True
        if lockB.acquire():
            print(self.name + '获取B锁')
            time.sleep(0.1)
            if lockA.acquire(timeout=4):
                print(self.name + '获取A锁,原来还有B锁')
                lockA.release()
            lockB.release()


if __name__ == '__main__':
    t1 = MyThread()
    t2 = MyThread()

    t1.start()
    t2.start()
