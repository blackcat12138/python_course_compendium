'''
    生产者与消费者：两个线程间的通信
        queue模块：提供了同步的、线程安全的队列类,包括FIFO队列Queue,
                LIFO队列LifoQueue,和优先级队列PriorityQueue,
                这些队列都实现了锁的原子操作。通过队列来实现线程间的同步。

        总结：
            进程共享数据与线程共享数据区别:
                进程是每个进程中都有一份
                线程是共同一个数据-->数据安全性问题
'''
import queue
import random
import threading
import time


def produce(q):
    i = 0
    while i < 10:
        num = random.randint(1, 100)
        q.put('生产者产生数据: %d' % num)
        print('生产者产生数据: %d' % num)
        time.sleep(1)
        i += 1
    q.put(None)
    # 完成任务
    q.task_done()


def consume(q):
    while True:
        item = q.get()
        if item is None:
            break
        print('消费者获取到：%s ' % item)
        time.sleep(4)
    # 完成任务
    q.task_done()


if __name__ == '__main__':
    q = queue.Queue(10)
    arr = []

    # 创建生产者
    th = threading.Thread(target=produce, args=(q,))
    th.start()

    # 创建消费者
    tc = threading.Thread(target=consume, args=(q,))
    tc.start()

    th.join()
    tc.join()

    print('END')
