"""
有一个多层嵌套列表A=[1,2,[3.4["434",[...]]]]
请写一段代码遍历A 中的每一个元素并打印出来

算法思想：递归
"""


def flat(nums):
    res = []
    for i in nums:
        if isinstance(i, list):
            res.extend(flat(i))
        else:
            res.append(i)
    return res


if __name__ == '__main__':
	alist=[1,[2,3,[4,5,[6,7,[8,[9,[10],11],12],13],14],15],16]
	a=flat(alist)
	print(a)
