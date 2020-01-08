"""
题目：把字符串中的空格替换成'20%'

方法1：直接使用Python字符串的内置函数
方法2：正则表达式
"""
import re


STR = "this is test text for replace"

new_str = STR.replace(' ', '20%')
print(new_str)


ret = re.compile(' ')
res = ret.sub('20%', STR)
print(res)
