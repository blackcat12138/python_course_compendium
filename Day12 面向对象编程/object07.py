'''
    封装
'''


class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def study(self, course_name):
        # 在类内部,通过"self.私有属性"访问
        print(f'{self.__name}正在学习{course_name}.')


stu = Student('江小白', 20)
stu.study('数学')
# 在类外部,通过"对象._Student__name"访问私有属性
print(stu._Student__name, stu._Student__age)
