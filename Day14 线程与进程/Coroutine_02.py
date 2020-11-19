'''
    greenlet 完成协程任务
'''

import time

from greenlet import greenlet


# 任务A
def a():
    for i in range(5):
        print('A' + str(i))
        gb.switch()
        time.sleep(0.1)


# 任务B
def b():
    for i in range(5):
        print('B' + str(i))
        gc.switch()
        time.sleep(0.1)


# 任务C
def c():
    for i in range(5):
        print('C' + str(i))
        ga.switch()
        time.sleep(0.1)


if __name__ == '__main__':
    ga = greenlet(a)
    gb = greenlet(b)
    gc = greenlet(c)

    ga.switch()
