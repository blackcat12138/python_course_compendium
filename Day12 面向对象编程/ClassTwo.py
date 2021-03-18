'''
    类中的初始化方法
'''


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print(f'{self.name}正在学习{course_name}.')

    def play(self):
        print(f'{self.name}正在玩游戏.')

# 在调用Student类的构造器创建对象时需传入两个参数
stu1 = Student("王大锤", 20)
stu2 = Student("uzi", 15)
stu1.study("数学")
stu2.play()
