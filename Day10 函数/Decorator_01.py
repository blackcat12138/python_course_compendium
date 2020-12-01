'''
    装饰器
        装饰器的特点:
            1.函数A作为参数出现（函数B就接收函数A作为参数）
            2.要有闭包的特点
        通过@decorate装饰的函数(被装饰函数),会作为参数传给装饰器,
        然后执行函数,最后将返回值又赋值给被装饰函数
'''


def func(number):
    a = 100

    def inner_func():
        nonlocal a
        nonlocal number
        number += 1
        for i in range(number):
            a += 1

        print('修改后的a:', a)

    return inner_func


# 调用func
fc = func(5)
fc()

# 函数作为参数
a = 50
f1 = func(a)
print(f1)
print('-----------------')


# 装饰器的定义
def decorator(func):
    a = 100
    print('wrapper外层打印测试')

    def wrapper():
        func()
        print('------->刷漆')
        print('------->铺地板', a)

    print('wrapper加载完成....')
    return wrapper


# 装饰器的使用
# huose()函数会作为参数传递给func()
@decorator
def house():
    print('毛坯房.......')


# def house1():
#     house()
#     print('刷漆')
#     print('铺地板')

house()
