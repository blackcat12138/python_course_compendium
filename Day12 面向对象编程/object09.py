'''
    动态属性
'''


class Student:
    __slots__ = ('name','age')

    def __init__(self, name, age):
        self.name = name
        self.age = age


stu = Student('uzi', 20)
# AttributeError: 'Student' object has no attribute 'sex'
stu.sex = '男'
