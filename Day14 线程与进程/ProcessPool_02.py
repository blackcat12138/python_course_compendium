'''
    阻塞式进程：添加一个执行一个任务,若一个任务不结束另一个任务就进不来。
'''
import os
import time
from multiprocessing import Pool

from random import random

def task(task_name):
    print('开始做任务', task_name)
    start = time.time()
    time.sleep(random() * 2)
    end = time.time()
    print('完成任务：{},用时：{},进度id:{}'.format(task_name, (end - start), os.getpid()))
    #return '完成任务：{},用时：{},进度id:{}'.format(task_name, (end - start), os.getpid())


# container = []
#
#
# # 回调函数
# def callback_func(n):
#     container.append(n)

if __name__ == '__main__':
    pool = Pool(5)

    tasks = ['lol', '斗地主', '吃饭', '睡觉', '生孩子']
    for i in tasks:
        pool.apply(task, args=(i,))

    pool.close()
    pool.join()

    print('over!!!!')
