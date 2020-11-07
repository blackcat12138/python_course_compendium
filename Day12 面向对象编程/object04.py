'''
    __str__：
        触发时机：打印对象名 自动触发取去调用__str__里面的内容
            注意：一定要在__str__方法中添加return,return后面内容就是打印对象看到内容
'''
class Cat:

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        return '姓名：'+self.name+'，年龄：'+str(self.age)


c=Cat('uzi',18)
print(c) # <__main__.Cat object at 0x000001F768EFC710>

# 单纯打印对象名称,出来的是一个地址.地址对于开发者没有意义
# 若想打印对象名,可以定义__str__魔术方法

c1=Cat('sofm',22)
print(c1)

'''
    总结：魔术方法
    重点:
        __init__  ：创建完空间后调用的第一个方法
        __str__
    了解:
        __new__ 作用：开辟空间
        __del__ 作用：没有指针引用时候会调用,不需要重写
        __call__ 作用：想不想将对象当成函数用  
'''