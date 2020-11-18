'''
    进程中的通信

'''

from multiprocessing import Queue

q = Queue(5)

q.put('A')
q.put('B')
q.put('C')
q.put('D')
# put() : 若queue中满了则只能等待,除非有'空位',则添加成功
q.put('E')
print(q.qsize())
if not q.full():  # 判断队列是否满 q.empty() 判断队列是否为空
    q.put('F', timeout=3)
else:
    print('队列满了！')

# 获取队列中的值
print(q.get(timeout=2))
print(q.get(timeout=2))
print(q.get(timeout=2))
print(q.get(timeout=2))
print(q.get(timeout=2))
if not q.empty():
    q.get(timeout=2)
else:
    print('队列为空')

q.put_nowait()
q.get_nowait()
