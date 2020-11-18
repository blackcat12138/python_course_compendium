'''
    线程是可以共享全局变量的
    python底层只要有线程默认加锁,这种锁GIL,这样即使是共享数据底层也会加锁
    GIL : 全局解释器锁,保证同一时刻只有一个线程可以执行。
    问题1：GIL何时将会释放
         (a).在遇到i/o操作时,会有时间闲置情况,造成cpu闲置的情况下释放GIL
         (b).设置ticks进行计数,当ticks数值达到100时将释放GIL
    问题2：互斥锁与GIL锁的关系
        GIL锁：保证同一时刻只有一个线程能使用cpu
        互斥锁：多线程时,保证修改共享数据时有序的修改,不会产生数据修改混乱。(不会造成数据不安全的情况)
    线程一般耗时操作,如爬虫、下载电影等
    进程一般计算量大的时候使用
'''
import threading
from time import sleep

ticket = 1000


def run1():
    global ticket
    for i in range(100):
        sleep(0.2)
        ticket -= 1


# def run2():
#     global ticket
#     for i in range(100):
#         ticket -= 1


if __name__ == '__main__':
    th1 = threading.Thread(target=run1, name='th1')
    th2 = threading.Thread(target=run1, name='th2')

    th1.start()
    th2.start()

    th1.join()
    th2.join()

    print('money:', ticket)
