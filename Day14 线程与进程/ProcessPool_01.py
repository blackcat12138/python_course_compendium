'''
    进程池：避免频繁创建进程
    非阻塞式：全部添加到队列中,立刻返回,
             并没有等待其他的进程完毕后才会结束,
             但回调函数是等待任务完成后才调用。
'''
import os
import time
from multiprocessing import Pool

# 非阻塞式进程
from random import random


def task(task_name):
    print('开始做任务', task_name)
    start = time.time()
    time.sleep(random() * 2)
    end = time.time()
    # print('完成任务：{},用时：{},进度id:{}'.format(task_name, (end - start), os.getpid()))
    return '完成任务：{},用时：{},进度id:{}'.format(task_name, (end - start), os.getpid())


container = []


# 回调函数
def callback_func(n):
    container.append(n)


if __name__ == '__main__':
    pool = Pool(5)

    tasks = ['lol', '斗地主', '吃饭', '睡觉', '生孩子']
    for i in tasks:
        pool.apply_async(task, args=(i,), callback=callback_func)

    # 添加任务结束
    pool.close()
    pool.join()  # 插队

    for c in container:
        print(c)
    print('over!!')
