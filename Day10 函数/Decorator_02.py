'''
    装饰器的参数（万能装饰器）
        1.python也可以支持多层装饰器（多个装饰函数装饰一个被装饰函数）调用按照就近原则输出
        2.带参数的装饰器,那么装饰器函数必须是在原来的基础上又加了一层函数（三层装饰器函数）
'''
import time


def decorate(func):
    def wrapper(*args, **kwargs):
        print('正在校验。。。。。')
        time.sleep(1)
        # 调用原函数
        func(*args, **kwargs)
        print('完成校验。。。。。')

    return wrapper


def outer(a):  # 第一层：负责接受参数的
    def decorate(func):  # 第二层：负责接收函数的
        def wrapper(*args):  # 第三层：负责接收函数的参数
            func(*args)
            print('--->铺砖...'.format(a))

        return wrapper  # 返回出的是：第三层

    return decorate  # 返回出的是：第二层


@decorate
def f1(n):
    print('-------f1-----', n)


@decorate
def f2(name, age):
    print('------f2-------', name, age)


@decorate
def f3(student, clazz='2012'):
    print('{}班级的学生：'.format(clazz))
    for stu in student:
        print(stu)


@outer(a=12)
def f4(time):
    print('我{}日期拿房子,是毛坯房。。。。'.format(time))


f1(5)
f2('uzi', 23)

student = ['ming', 'sofm', 'mlxg']
f3(student)

f4('20201201')
