'''
    面向对象中的多态
'''


class Peason:
    def __init__(self, name):
        self.name = name

    def feed_pet(self, pat):
        # isinstance(obj,类)：判断obj是否是类的对象或判断obj是否是该类子类的对象
        if isinstance(pat,Pat):
            print('{}喜欢养宠物:{},昵称是：'.format(self.name,pat.role,pat.nname))
        else:
            print('不是宠物类型的，不能养。。。。。。')


class Pat:
    role = 'uzi'

    def __init__(self, nname, age):
        self.nname = nname
        self.age = age

    def show(self):
        print('昵称：{},年龄:{}'.format(self.nname, self.age))


class Cat(Pat):
    role = '猫'

    def catch_mouse(self):
        print('抓老鼠。。。。。')


class Dog(Pat):
    role = '狗'

    def wathc_house(self):
        print('看家。。。。。。')

class Tiger:
    def eat(self):
        print('可以吃人。。。。。。')

# 创建对象
cat=Cat('feifei',2)

dog=Dog('旺财',33)

tiger=Tiger()

ps=Peason('wang')

ps.feed_pet(cat)

print('=========================')
person=Peason('jiajia')
person.feed_pet(tiger)

