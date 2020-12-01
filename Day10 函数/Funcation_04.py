'''
    内部函数、闭包
        内部函数：与局部变量类似,都是定义在函数内部的;
             1.内部函数定义后需要对其进行调用才能访问执行函数内的操作;
             2.内部函数可以访问修改外部函数定义的可变变量,若想修改外部函数定义的不可变变量,
               就需要通过nonlocal关键字进行声明该变量。
             3.内部函数修改全局的不可变变量时,也需要在内部函数通过global关键字声明该变量
             4.内置函数
                    globals()：查看声明的全局变量,以字典的形式输出
                    locals()：查看声明的本地变量,以字典的形式输出(会有系统的键值对)

        闭包：在外部函数中定义了内部函数,通过返回值return关键字将内部函数名返回(不加括号),
              实现外部调用访问内部函数的操作;
              保存返回闭包时的状态(外层函数变量)。
                  语法格式如下：
                    def 外部函数()：
                        ......
                        def 内部函数()：
                            .............
                        return 内部函数

                    变量=外部函数()
                    变量()

        闭包缺点:
            a.闭包引用了外部函数的局部变量没有及时释放,消耗内存
            b.延长了作用域,并且可以使用同级作用域,所以作用域没那么直观
        闭包优点:
            a.闭包优化了变量,原先要类对象完成的,闭包也可以完成
            b.代码简洁,便于阅读


'''

x = 200


def func_01():
    # 声明局部变量
    n = 100  # 不可变变量
    list1 = [5, 1, 6, 4]  # 可变变量

    # 声明内部函数
    def inner_func():
        global x
        nonlocal n
        # 对list1局部变量中的元素进行加5操作
        for index, i in enumerate(list1):
            list1[index] = i + 5
        list1.sort()

        # 修改外部函数的不可变变量
        n += 111
        x -= 10

    # 调用内部的函数
    inner_func()

    print(list1)
    print(n)
    print(x)


# 调用func()
func_01()
print('========================================')


# 闭包1
def func_02(a, b):
    c = 300

    def inner_fnnc():
        s = a + b + c
        print(s)

    return inner_fnnc


# 当多次调用外部函数赋值参数,内部函数返回的参数不会因为多次调用而改变
y = func_02(2, 1)
y2 = func_02(3, 4)
print(y)
print(y2)
y2()
y()
print('================================')


# 闭包2
def generate_count():
    container = [0]

    def add_one():
        container[0] = container[0] + 1
        print('当前是第{}次访问'.format(container[0]))

    return add_one


# 内部函数相当于一个计数器
counter = generate_count()
counter()
counter()
counter()
print('=================================')


# 闭包3--同级访问
def func_03():
    a = 100

    def inner_func1():
        b = 90
        s = a + b
        print(s)

    def inner_func2():
        inner_func1()
        print('------------->inner_func2', a)
        return 'hello'

    return inner_func2


f = func_03()
print(f)
ff = f()
print(ff)
