'''
  __init__：初始化魔术方法
        触发时机：初始化对象时触发(不是实例化触发,但是和实例化在一个操作中)
  __new__： 实例化魔术方法
        触发时机：在实例化对时触发
  __call__：对象调用方法
        触发时机：将对象当成函数使用时,会默认调用该函数中内容
  __del__：delete的缩写 析构魔术方法
        触发时机：当对象没有用（没有任何变量引用）的时候被触发
        (a).对象赋值：
            p=Person()
            p1=p
            p和p1共同指向同一个地址
        (b).删除地址的引用
            del p1    删除p1对地址的引用
        (c).查看对地址的引用次数:
            import sys
            sys.getrefcount(p)
        (e).当一块空间没有任何引用,默认执行__del__
'''


class Person:
    def __init__(self, name):
        print('---------->init', self)
        self.name = name

    def __new__(cls, name):
        print('-------->new')
        return object.__new__(cls)

    def __call__(self, name):
        print('----------->call')
        print('执行对象得到参数是：', name)

    def __del__(self):
        print('------del---->')



p = Person('uzi')
p1 = p
p2 = p
print(p1.name)
print(p2.name)

p1.name = 'tom'
p('hello')

del p2