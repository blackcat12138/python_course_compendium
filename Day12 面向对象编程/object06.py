'''
    通过装饰器来处理私有属性
'''


class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    # 先有getxxx
    @property
    def age(self):
        return self.__age

    # 再有set,因为set依赖get
    @age.setter
    def age(self, age):
        if age > 0 and age < 120:
            self.__age = age
        else:
            print('年龄不在范围内')

    # def setAge(self, age):
    #     if age > 0 and age < 120:
    #         self.__age = age
    #     else:
    #         print('年龄不在范围内')
    #
    # def getAge(self):
    #     return self.__age

    def __str__(self):
        return '姓名：{},年龄:{}'.format(self.name, self.__age)


s1 = Student('huahua', 30)
s1.name = 'qingqing'
print(s1.name)

# 私有化赋值
# s1.setAge(40)
# print(s1.getAge())

print(s1.age)
s1.age = 130


class Tvshow:
    def __init__(self, show):
        self.__show = show

    @property
    def show(self):
        print('------------>正在表演')
        return self.__show


tv = Tvshow('牛宝')
print(tv.show)
# tv.show='相声'
