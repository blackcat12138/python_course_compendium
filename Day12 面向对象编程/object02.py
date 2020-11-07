'''
    类方法特点:
        1.定义需要依赖装饰器@classmethod
        2.类方法中参数不是一个对象,而是类
        3.类方法中只可以使用类属性
        4.类方法中可否使用普通方法? 不能
    类方法作用:
        因为只能访问类属性和类方法，
        所以可以在对象创建之前,若需要完成一些动作(功能)
    静态方法特点：类似于类方法
        1.需要装饰器@staticmethod
        2.静态方法是无需传递参数（cls,self）
        3.只能访问类的属性和方法,对象的是无法访问的
        4.加载时机同类方法
总结:
  类方法与静态方法的区别
      不同:
        1.装饰器不同
        2.类方法是有参数的,静态方法没有参数
     相同:
        1.只能访问类的属性和方法，对象的是无法访问的
        2.都可以通过类名调用访问
        3.都可以再创建对象之前使用,因为是不依赖于对象
  普通方法与两者的区别
    不同：
        1.没有装饰器
        2.普通方法永远是要依赖对象,因为每个普通方法都有一个self
        3.只有创建了对象才可以调用普通方法,否则无法调用。
'''


class Dog:
    __age = 18
    type='狗'

    # 通过__init__初始化的特征
    def __init__(self, nickname,age,color):
        self.nickname = nickname
        self.age=age
        self.color=color

    def run(self):  # self 对象
        print('{}在院子里跑来跑去！'.format(self.nickname))

    def eat(self,food):
        print('{}喜欢吃饭｛｝。。。。。。。。'.format(self.nickname,food))
        self.run()  # 类中方法的调用，需要通过self.方法名()

    def catch_mouse(self,color,weight):
        print('{},抓一只{}kg的,{}的大老鼠'.format(self.nickname,weight,color))

    def sleep(self,hour):
        if hour<5:
            print('继续睡觉吧')
        else:
            print('起床抓老鼠')

    def show(self):
        # print('------------>', Dog.age)
        print('狗的详细信息：')
        print(self.nickname,self.age,self.color)

    @classmethod
    def test(cls):  # cls class
        # print(cls) # <class'__main__.Dog'>
        # print(cls.nickname)
        # self.run()
        print('---------->类方法')
        cls.__age=20

    @classmethod
    def show_age(cls):
        print('修改后的年龄是：',cls.__age)

    @staticmethod
    def update_age():
        print('------->静态方法')
        print(Dog.__age)

# d=Dog('旺财')
#
# d.run() # 调用run方法
#
# d.test()

Dog.test()
Dog.show_age()
Dog.update_age()

print('---------------------------')
# 创建对象
dog1=Dog('uzi',2,'黄色')
# 通过对象调用方法
dog1.catch_mouse('黑色',3)

dog1.eat('骨头')

dog1.show()