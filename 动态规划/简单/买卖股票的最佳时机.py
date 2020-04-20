"""
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。

注意你不能在买入股票前卖出股票。

示例 1:

输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
示例 2:

输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。


解题：
题目的假设比较简单，一天只能进行一次买或卖，且只有买了才能卖。那么我们只需要计算每一天可以得到的最低的买入价以及可操作的最高卖出价，
计算它们的差值就可以得到每天可知的最高收入，然后取最大值即可。

以 Example 1 为例，输入是每一天的股票价格[7,1,5,3,6,4]，那么第一天只能以 7 买入，第二天可以以 1 买入，第三天的价格5高于第二天价格 1，
所以还是在第二天以 1 的价格买入，以此类推，每一天的最优买入价是[7,1,1,1,1,1]；买入价需要从第一天向后推算，那么卖出价需要从最后一天向前推算：
在第六天只能以 4 卖出，在第五天可以以 6 卖出，第四天的价格为 3，但是可以等到第五天再卖，所以第四天的可操作的最高卖出价6，
以此类推得到每一天可操作的最高卖出价是 [7,6,6,6,6,4]。那么，每一天可知的最大收益用最高卖出价减去最低买入价即可：[0,5,5,5,5,4]，
对每一天的最大收益取最大值，可以得到只进行一次买卖的整体最大收益。

"""

class Solution:
    def maxProfit(self, prices):
        # 方法一：超出时间限制
        # k = len(prices)
        # res = 0
        # if k<2:
        #     return 0
        # for i in range(k-1):
        #     for j in range(i, k):
        #         if prices[j]>prices[i]:
        #             res = max(prices[j] - prices[i], res)

        # return res


        # 方法二：动态规划
        # k = len(prices)

        # if k < 2:
        #     return 0
        # buying_prices = prices.copy()
        # selling_prices = prices.copy()

        # # 计算每一天的买入价最优解
        # buying_price = prices[0]
        # for i in range(k):
        #     if buying_price > prices[i]:
        #         buying_price = prices[i]
        #     buying_prices[i] = buying_price

        # # 计算每一天的卖出最优解
        # selling_price = prices[-1]
        # for i in range(k-1, -1, -1):  # 倒着轮回
        #     if selling_price < prices[i]:
        #         selling_price = prices[i]
        #     selling_prices[i] = selling_price

        # max_profit = max(y - x for x, y in zip(buying_prices, selling_prices))
        # return max_profit

        # 方法三：方法二的优化
        # if len(prices) < 2:
        #     return 0
        # max_profits = 0  # 最大收益
        # buying_price = prices[0]  # 最优买入
        # for i in range(len(prices)):
        #     if prices[i] < buying_price:
        #         buying_price = prices[i]
        #     else:
        #         profit = prices[i] - buying_price
        #         if profit > max_profits:
        #             max_profits = profit

        # return max_profits

        # 方法四：好于以上三种
        """
        :type prices: List[int]
        :rtype: int
        """
        min_p, max_p = 999999, 0
        for i in range(len(prices)):
            min_p = min(min_p, prices[i])
            max_p = max(max_p, prices[i] - min_p)
        return max_p


if __name__ == '__main__':
    # prices = [1, 2]
    prices = [7,1,5,3,6,4]
    solution = Solution()
    res = solution.maxProfit(prices)
    print(res)