class KLs(object):
    def foo(self, x):
        print('executing foo(%s,%s)' % (self, x))

    @classmethod
    def class_foo(cls, x):
        print('executing class_foo(%s,%s)' % (cls, x))

    @staticmethod
    def static_foo(x):
        print('executing static_foo(%s)' % x)

ik=KLs()

# 实例方法
ik.foo(1)
print(ik.foo)
print('=================')

# 类方法
ik.class_foo(1)
KLs.class_foo(1)
print(ik.class_foo)
print('=================')

# 静态方法
ik.static_foo(1)
KLs.static_foo('hi')
print(ik.static_foo)
