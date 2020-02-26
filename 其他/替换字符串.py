# a = “abbbccc”，用正则匹配为abccc,不管有多少b，就出现一次
import re


a = "abbbccc"
res = re.sub(r'b+', 'b', a)
print(res)