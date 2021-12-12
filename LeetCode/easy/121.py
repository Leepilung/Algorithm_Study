# LeetCode 121. Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, min_price = 0, 1000000
        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            profit = max(profit, profit)
        return profit