'''
    进程的创建

    导入模块：from multiprocessing import Process
        process=Process(target=函数,name=进程名称,args=(给函数传递参数))
        process 对象
        对象调用方法:
            process.start() 启动进程并执行任务
            process.run() 只是执行了任务但没有启动进程
            terminate() 终端,终止进程。

    多进程对全局变量访问,在每个全局变量中都放一个m变量,
    保证每个进程访问变量互不干扰
    m=1      # 不可变类型
    list1=[] # 可变类型
'''

import os
from multiprocessing import Process
from time import sleep


def task1():
    while True:
        sleep(1)
        print('--------->这是任务1',os.getpid(),'----->',os.getppid())


def task2():
    while True:
        sleep(2)
        print('---------->这是任务2',os.getpid(),'----->',os.getppid())


if __name__ == '__main__':
    # task1()
    # tesk2()
    # 子进程
    p = Process(target=task1, name='任务1')
    p.start()
    print(p.name)
    p1 = Process(target=task2, name='任务2')
    p1.start()
    print(p1.name)

    print('----------------')
    print('****************')