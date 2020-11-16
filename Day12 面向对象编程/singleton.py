'''
    开发模式中的单例模式:单个对象;每次创建的对象都共有一个内存地址,这样对内存优化
'''


class Singleton:
    # 私有化实例
    __instance = None
    name = 'uzi'

    # 重写__new__
    def __new__(cls):
        print('------->__new__')
        if cls.__instance is None:
            print('--->1')
            cls.__instance = object.__new__(cls)
            print(cls.__instance)
            return cls.__instance
        else:
            print('----->2')
            return cls.__instance

    def show(self, n):
        print('-------->show', Singleton.name, n)


s = Singleton()
s1 = Singleton()

print(s)
print(s1)

print('==========================')
s.show(4)
s1.show(5)
