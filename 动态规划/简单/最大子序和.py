"""
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

"""

class Solution:
    def maxSubArray(self, nums):
        # 方法一：暴力法
        # k = len(nums)
        # res = min(nums)
        # for i in range(k):
        #     _ = 0
        #     for j in range(i, k):
        #         _ += nums[j]
        #         res = max(res, _)
        # return res

        # 方法二
        """
        :type nums: List[int]
        :rtype: int
         """
        for i in range(1, len(nums)):
            nums[i]= nums[i] + max(nums[i-1], 0)  # 此法相当于将列表中每一个数都变成当前位置数和前一个数相加的结果。
        return max(nums)

if __name__ == '__main__':
    # nums = [-2,1,-3,4,-1,2,1,-5,4]
    nums = [-1, 2, -3, 1, 2]
    solution = Solution()
    res = solution.maxSubArray(nums)
    print(res)