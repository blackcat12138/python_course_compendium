'''
    进程 > 线程 > 协程
    协程：微线程,应用在耗时操作（跟网络请求、网络下载[爬虫]、io操作）,
         当阻塞后能够快速切换,即只有遇到耗时操作立马进行切换,高效的利用CUP和资源
'''
import time


def task1():
    for i in range(3):
        print('A' + str(i))
        yield
        time.sleep(1)


def task2():
    for i in range(3):
        print('B' + str(i))
        yield
        time.sleep(2)
        _


if __name__ == '__main__':
    g1 = task1()
    g2 = task2()

    while True:
        try:
            next(g1)
            next(g2)
        except:
            break
