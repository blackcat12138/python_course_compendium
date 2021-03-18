'''
    类方法、实例方法、静态方法的区别
'''


class cat:
    __age = 23
    type = '猫'

    def __init__(self, name, age, color):
        self.age = age
        self.color = color
        self.name = name

    # self对象
    def run(self):
        print('{}在院子中跑'.format(self.name))

    def eat(self, foot):
        print('{}喜欢吃{}'.format(self.name, foot))
        # 类中调用方法,通过self.方法名()
        self.run()

    @classmethod

