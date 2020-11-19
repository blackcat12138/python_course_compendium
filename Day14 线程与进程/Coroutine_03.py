'''
    gevent 完成协程任务

    由于greenlet实现协程通过调用switch()是人工切换任务,不够智能。
    python还提供了gevent模块,实现自动切换任务。

    原理:
        当greentlet遇到IO操作时,会自动切换到其他的greenlet,等待IO完成,
        在适当的时候切换回来继续执行。
        由于IO操作非常耗时,经常使程序处于等待状态,当有个gevent后可以实现自动切换协程,
        保证总有greenlet在运行,而不是等待IO

'''

import time
import gevent
from gevent import monkey

monkey.patch_all()

# 任务A
def a():
    for i in range(5):
        print('A' + str(i))
        time.sleep(0.1)


# 任务B
def b():
    for i in range(5):
        print('B' + str(i))
        time.sleep(0.1)


# 任务C
def c():
    for i in range(5):
        print('C' + str(i))
        time.sleep(0.1)


if __name__ == '__main__':
    g1 = gevent.spawn(a)
    g2 = gevent.spawn(b)
    g3 = gevent.spawn(c)

    g1.join()
    g2.join()
    g3.join()

    print('-----------------')
