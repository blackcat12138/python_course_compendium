'''
    自定义进程
'''
from multiprocessing import Process


class MyProcess(Process):
    def __init__(self, name):
        super(MyProcess, self).__init__()
        self.name = name

    # 重写run方法
    def run(self):
        n = 1
        while True:
            # print('进程名称：',self.name)
            print('{}--------->自定义进程,n:{}'.format(n, self.name))
            n += 1


if __name__ == '__main__':
    p1 = MyProcess('uzi')
    # 开新进程,并且执行run()
    p1.start()

    p2 = MyProcess('ming')
    p2.start()
