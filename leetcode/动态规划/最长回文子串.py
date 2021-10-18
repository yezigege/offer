"""
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"

思想：回文就是 str[i] == str[j]
"""
class Soluation(object):
    def longestPalindrome(self, s):
        # 方法一：
        size = len(s)
        if size < 2:
            return s

        dp = [[False for _ in range(size)] for _ in range(size)]

        max_len = 1
        start = 0

        for i in range(size):
            dp[i][i] = True

        for j in range(1, size):
            for i in range(0, j):
                if s[i] == s[j]:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = False

                if dp[i][j]:
                    cur_len = j - i + 1
                    if cur_len > max_len:
                        max_len = cur_len
                        start = i
        return s[start:start + max_len]


        # 方法二：
        # str_length = len(s)
        # max_length = 0
        # start = 0
        # for i in range(str_length):
        #     if i - max_length >= 1 and s[i - max_length - 1:i + 2] == s[i - max_length - 1:i + 2][::-1]:
        #         start = i - max_length - 1
        #         max_length += 2
        #         continue
        #     if i - max_length >= 0 and s[i - max_length:i + 2] == s[i - max_length:i + 2][::-1]:
        #         start = i - max_length
        #         max_length += 1
        # return s[start:start + max_length+1]

        # 方法三：暴力匹配
        # 特判
    #     size = len(s)
    #     if size < 2:
    #         return s

    #     max_len = 1
    #     res = s[0]

    #     # 枚举所有长度大于等于 2 的子串
    #     for i in range(size - 1):
    #         for j in range(i + 1, size):
    #             if j - i + 1 > max_len and self.__valid(s, i, j):
    #                 max_len = j - i + 1
    #                 res = s[i:j + 1]
    #     return res

    # def __valid(self, s, left, right):
    #     # 验证子串 s[left, right] 是否为回文串
    #     while left < right:
    #         if s[left] != s[right]:
    #             return False
    #         left += 1
    #         right -= 1
    #     return True


if __name__ == '__main__':
    solution = Soluation()
    res = solution.longestPalindrome('babad')
    print(res)