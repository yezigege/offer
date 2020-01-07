"""
使用类的方式来创建单例
"""


class SingleTon(object):
    _instance = None

    def __new__(cls, *args):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


class MyClass(SingleTon):
    class_val = 22

    def __init__(self, val):
        self.val = val

    def obj_fun(self):
        print(self.val, 'obj_fun')

    @staticmethod
    def static_fun():
        print('staticmethod')

    @classmethod
    def class_fun(cls):
        print(cls.class_val, 'classmethod')


if __name__ == '__main__':
    a = MyClass(1)
    b = MyClass(2)
    print(a is b)   # True
    print(id(a), id(b))  # 4367665424 4367665424
    # 类型验证
    print(type(a))  # <class '__main__.MyClass'>
    print(type(b))  # <class '__main__.MyClass'>
