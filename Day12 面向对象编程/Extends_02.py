'''
    is a : base class 分类 基类
    继承:
        Student、Employee,Doctor -->
        都属于Person相同代码-->代码冗余,可读性不高
        将相同代码提取-->Person类
        Student、Employee,Doctor --> 继承Person

        class Student(Person):
            pass
    继承特点：
        1.若类中不定义__init__,先找自己再找父类 super class的__init__
        2.若类继承父类也需要定义自己的__init__,就需要在当前类的__init__调用父类的__init__
        3.调用父类__init__方式如下：
            super().__init__(参数)
            super(类名,对象).__init__(参数)
        4.若父类有eat(),子类也定义一个eat方法，默认查找的原则:先找当前类,再找父类
            s.eat()
            override：重写（覆盖）
            父类提供的方法不能满足子类的需求,就需要在子类中定义一个同名的方法,
            而这种行为称为重写。
        5.子类的方法中也可以调用父类的方法：
            super().方法名(参数)
'''


class Person:
    # def __init__(self):
    #     self.name='uzi'
    #     self.age=12
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(self.name + '正在吃饭。。。')


class Student(Person):
    # 调用父类的方法
    def __init__(self, name, age, clazz):
        print('------------>init魔术方法')
        super().__init__(name, age)  # super() 父类对象
        self.clazz = clazz

    def study(self, course):
        print('{}正在学习{}课程'.format(self.name, course))

    def eat(self, food):
        super().eat()
        print(self.name + '正在吃饭。。。。喜欢吃:' + food)


class Emloyee(Person):
    def __init__(self, name, age, manager):
        super().__init__(name, age)
        self.manager = manager


class Doctor(Person):
    def __init__(self, name, age, patients):
        super(Doctor, self).__init__(name, age)
        self.patients = patients


s = Student('mlxg', 18, '1904')
s.eat('包子')
s.study('python语言')

e = Emloyee('sofm', 23, 'king')
e.eat()

lists = ['厂长', 'ming', 'ning', 'tian']
d = Doctor('doss', 53, lists)
d.eat()
