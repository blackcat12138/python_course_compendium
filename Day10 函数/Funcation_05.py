'''
    值传递与引用传递
'''


def test1(c):
    print('test before')
    print(id(c))
    c += 1
    print('test after')
    print(id(c))
    return c


c = 1
test1(c)
print(c)

print("==================")

# def add(a):
#     a=2
# a=1
# add(a)

l1 = [1, 2, 3]
l2 = [1, 2, 3]
a = 1
b = 1
print(id(l1))
print(id(l2))
print(id(a))
print(id(b))

print("---------------------")


def demo(obj):
    obj += obj
    print("形参值为：", obj)


print("-----------值传递-------")
a = "C语言中文网"
print("a的值为：", a)
demo(a)
print("实参值为：", a)
print("----------引用传递---------")
a = [1, 2, 3]
print("a的值为：", a)
demo(a)
print("实参值为:", a)
