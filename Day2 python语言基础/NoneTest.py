'''
    None、is None、==的比较
'''
L = []
l = ''
x = None
# print中的逗号输出为空格
print(L is None, l is None)
print(x is None)
print("====================")

a=None
b=None
# 比较a对象与b对象的地址值是否相等
print(id(a)==id(b))

class test():
    def __eq__(self, other):
        return True

t=test()
print(t is None)
print('-----------------')
t=None
print(t==None)