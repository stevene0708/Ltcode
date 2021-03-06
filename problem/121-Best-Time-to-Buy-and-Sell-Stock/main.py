"""
    Author: Weng Xiang Heng
    Date: 2021/10/26
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = 10000000
        
        for price in prices:
            if(min_price > price):
                min_price = price
            if(max_profit < (price - min_price)):
                max_profit = price - min_price
        
        return max_profit 