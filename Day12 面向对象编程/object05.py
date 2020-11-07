'''
私有化
    封装：1.私有化属性 2.定义公有set和get方法
    __属性：就是将属性私有化，访问范围仅仅限于类中
    私有化的优点:
        1.隐藏属性不被外界随意修改
        2.通过函数是可以修改
            def setXXX(self.xxx):
            3.筛选赋值的内容
                if xxx是否符号条件
                    赋值
                else:
                    不赋值
        4.若想获取具体的某个属性
            使用get函数
                def getXXX(self):
                    return self.__xxx
'''


class Student:
    __age = 18  # 类属性

    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        self.__score = 89

    # 定义公有set和get方法
    # set是为了赋值
    def setAge(self, age):
        if age > 0 and age <= 120:
            self.__age = age
        else:
            print('年龄不在范围内')

    # get是为了取值
    def getAge(self):
        return self.__age

    def setName(self):
        pass

    def getName(self):
        return self.__name

    def __str__(self):
        return '姓名：{},年龄:{}，分数；{}'.format(self.__name, self.__age, self.__score)


s1 = Student('uzi', 18)
print(s1)
s1.age = 21
s1.__score = 100
print(s1)
s1.setAge(120)

s2 = Student('sofm', 20)
print(s2)

print(s1.getAge())

print(dir(s1))
print(dir(Student))

print(__name__)

print(s1._Student__age)

print(s1.__dir__())

