'''
    匿名函数--lambda
    lambda：是指一类无需定义标识符(函数名)的函数或子程序。
            可以接收任意多个参数(包括可选参数)并且返回单个表达式的值。
    语法格式：lambda arg1,arg2..argn: expression
    匿名函数通过func进行接收。
'''

from functools import reduce


# 传入多个参数的lambda函数,通过lambda来实现
def sum(x, y):
    return x + y


p = lambda x, y: x + y
print(p(4, 6))


# 函数中嵌入lambda
def new_func(x):
    return (lambda y: x + y)


t = new_func(3)
u = new_func(2)
print(t(3))
print(u(3))
print('=================================')

# lambda函数+filter函数 filter()：根据一定的条件对给定的列表进行过滤。
my_list = [2, 3, 4, 5, 6, 7, 8]
new_list = list(filter(lambda a: (a / 3 == 2), my_list))
print(new_list)

# lambda函数+map函数    map()：给定的列表值依次迭代返成一个新列表。
new_list_01 = list(map(lambda a: (a / 3 != 2), my_list))
print(new_list_01)

# lambda函数+reduce函数     reduce()：对参数序列中元素进行积累。
print(reduce(lambda a, b: a + b, [23, 21, 45, 98]))

# lambda函数+max函数
new_list_02 = ({'a': 10, 'b': 20}, {'a': 13, 'b': 20}, {'a': 9, 'b': 20}, {'a': 29, 'b': 20})
m = max(new_list_02, key=lambda x: x['a'])
print('列表中最大的值：', m)

print('===============================')
# lambda函数+sorted函数
students = [
    {'name': 'uiz', 'age': 20},
    {'name': 'ming', 'age': 18},
    {'name': 'mxlg', 'age': 17},
    {'name': 'sofe', 'age': 21},
]
std = sorted(students, key=lambda x: x['age'], reverse=True)
print(std)

# 实现1000的阶乘
print(reduce(lambda x, y: x * y, range(1, 1001)))

print('==================================')
# lambda函数+if语句
func = lambda x: x if x % 2 == 0 else x + 1
result = func(5)
print(result)
