"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
注意：给定 n 是一个正整数。

========================================================
分析：假定n=10,首先考虑最后一步的情况,要么从第九级台阶再走一级到第十级,
要么从第八级台阶走两级到第十级,因而,要想到达第十级台阶,最后一步一定是从第八级或者第九级台阶开始.
也就是说已知从地面到第八级台阶一共有X种走法,从地面到第九级台阶一共有Y种走法,那么从地面到第十级台阶一共有X+Y种走法.
即F(10)=F(9)+F(8)
     分析到这里,动态规划的三要素出来了.
        边界:F(1)=1,F(2)=2
        最优子结构:F(10)的最优子结构即F(9)和F(8)
        状态转移函数:F(n)=F(n-1)+F(n-2)
"""

# 方法一：动态规划
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n <= 2:
            return n
        a = 1  # 边界
        b = 2  # 边界
        temp = 0
        for i in range(3, n+1):
            # a, b = b, a+b
            temp = a+b  # 状态转移
            a = b  # 最优子结构
            b = temp  # 最优子结构
        return temp


solution = Solution()
print(solution.climbStairs(10))



# 方法二：递归
def temp(n):
    if n <= 2:
        return n
    a = 1
    b = 2
    temps = 0
    return temp(n-1) + temp(n-2)

print("===> ", temp(10))


# 方法二改进版
def temp(n):
    if n <= 2:
        return n
    a, b = 1, 2
    for i in range(3, n+1):
        return temp(n-1) + temp(n-2)

print(f"==={temp(10)}===")