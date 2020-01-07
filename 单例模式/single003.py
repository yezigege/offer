"""
使用模块来制作单例
"""


class SingleTon(object):

    def __init__(self, val):
        self.val = val


single = SingleTon(2)
