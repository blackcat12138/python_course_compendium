'''
    可变参数与关键字参数
           1.可变参数的定义方式：
                def add(*args):
                    pass
            可变参数必须放在后面：(name,*args)

            *arge-->元组

          2.关键字参数的定义方式：
            def func(**kwargs)：
                print(kwargs)
            func(a=1,b=2,c=3)

            **kwargs-->字典


'''


# 定义方式:
def add(*args):  # argument 参数
    # print(args)
    sum = 0
    if len(args) > 0:
        for i in args:
            sum += i
        print('和：', sum)
    else:
        print('没有元素可计算：', sum)


add()  # 空元组
add(1)
add(1, 2)
add(1, 2, 34, 5)
print('-------------------------')


def aff(a, b=10, c=4):  # 关键字参数：默认设置的参数
    result = a + b + c
    print(result)


aff(5)
# 实际参数将会覆盖形式参数中的默认设置的参数值 7覆盖b原来的默认值
aff(4, 7)
# 实际参数可以通过关键字的key进行赋值,实现指定参数赋值 原先默认c=4被c=6覆盖
aff(2, c=6)
print('-------------------------------')


def func(*args, **kwargs):
    print(args, kwargs)


func(a=1, b=2, c=3)
func()
func(a=1)
func(a=1, b=2)
dict1 = {'001': 'python', '002': 'java', '003': 'scale'}
dict2 = ['uiz', 'ming', 'sofm']
# 拆包：通过 **变量名 的形式将字典进行拆成 '001'='python' 的形式,实现实际参数传递
func(**dict1)
func(*dict2, **dict1) 
print('-------------------------------')

# 练习:打印每位同学姓名和年龄
students = {'001': ('uzi', 20), '002': ('马保国', 69), '003': ('蔡徐坤', 21)}


def print_boy(name, **persons):
    print('{}喜欢的人是：'.format(name))
    if isinstance(persons, dict):
        for name, age in persons.values():
            print('{}的年龄是：{}'.format(name, age))


print_boy('卢本伟', **students)

print('--------------------------')


# 形式参数中的可变参数和关键字参数必须放在后面    (a,b,*args,**kwargs)
def akk(a, b, *c, **d):
    print(a, b, c, d)


akk(1, 2)  # 1 2 () {}
akk(1, 2, 3, 4)  # 1 2 (3,4) {}
akk(1, 2, x=100, y=200)  # 1 2 () {'x': 100, 'y': 200}
akk(1, 2, 3, x=300)  # 1 2 (3,) {'x': 300}
