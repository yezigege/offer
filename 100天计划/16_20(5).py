"""
动态规划 - 适用于有重叠子问题和最优子结构性质的问题
使用动态规划方法所耗时间往往远少于朴素解法(用空间换取时间)
"""

#
# def fib(num, temp={}):
#     """用递归计算Fibonacci数"""
#     if num in (1, 2):
#         return 1
#     try:
#         return temp[num]
#     except KeyError:
#         temp[num] = fib(num - 1) + fib(num - 2)
#         return temp[num]
#
#
# num = fib(11)
# print(num)


"""
子列表元素之和的最大值
例如,如果给定列表是[-2,1,-3,4,-1,2,1,-5,4],则具有最大总和的相邻子列表为[4,-1,2, 1],总和6
"""


# def main():
#     items = list(map(int, input().split()))
#     size = len(items)
#     overall, partial = {}, {}
#     overall[size - 1] = partial[size - 1] = items[size - 1]
#     for i in range(size - 2, -1, -1):
#         partial[i] = max(items[i], partial[i + 1] + items[i])
#         overall[i] = max(partial[i], overall[i + 1])
#     print(overall[0])
#
#
# if __name__ == '__main__':
#     main()

import time
from typing import List


items = [1, 3, 9, 4, 10]
sums = 7


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        _dict = {}
        for i, m in enumerate(nums):
            if _dict.get(target - m) is not None:
                return [_dict.get(target-m), i]
            _dict[m] = i

d = time.time()
so = Solution()
a, b = so.twoSum(items, sums)
e = time.time()
f = e - d
print(a, b, f)
