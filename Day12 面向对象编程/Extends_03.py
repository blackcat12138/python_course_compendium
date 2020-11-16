'''
    python中的多继承：在子类参数中有多个父类，通过','符号相隔。
    多继承的搜索顺序：
        经典类(python2中 深度优先)
        新式类(python3中 广度优先)
    在python2中才能显示出经典类和新式类的不同
'''


# class Person:
#     def __init__(self,name):
#         self.name=name
#
#     def eat(self):
#         print('-------->eat1')
#
#     # 同名不同参的方法 后面的方法将会覆盖前面的方法
#     def eat(self,foot):
#         print('------->eat:',foot)
#
# p=Person('jack')
# p.eat('包子')

class Base:
    def test(self):
        print('-------->>base')


class A(Base):
    def test(self):
        print('--------->>AAAAA')


class B(Base):
    def test1(self):
        print('---------->BBBBBBB')


class C(A, B, Base):
    def test2(self):
        print('-------->CCCCCCCCCC')


class D(A, B, C):
    pass


# c = C()
# c.test()
# c.test1()
# c.test2()

d = D()
d.test()
