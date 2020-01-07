from 单例模式.single003 import single


a = single
b = single
print(a.val, b.val)
print(a is b)
a.val = 233
print(a.val, b.val)
