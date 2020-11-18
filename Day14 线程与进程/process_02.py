'''
    进程的任务参数传递
'''
import os
from multiprocessing import Process
from time import sleep


def task1(s, name):
    while True:
        sleep(s)
        print('--------->这是任务1', os.getpid(), '----->', os.getppid(), name)


def task2(s, name):
    while True:
        sleep(s)
        print('---------->这是任务2', os.getpid(), '----->', os.getppid(), name)


number = 1
if __name__ == '__main__':
    # task1()
    # tesk2()
    # 子进程
    p = Process(target=task1, name='任务1', args=(1, 'uzi'))
    p.start()
    print(p.name)
    p1 = Process(target=task2, name='任务2', args=(2, 'ming'))
    p1.start()
    print(p1.name)

    while True:
        number += 1
        sleep(0.2)
        if number == 20:
            p.terminate()
            p1.terminate()
            break
        else:
            print('---------->number', number)

    print('----------------')
