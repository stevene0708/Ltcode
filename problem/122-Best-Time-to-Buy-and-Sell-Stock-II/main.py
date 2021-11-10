"""
    Date: 2021/11/10
    Key: Mutiple transaction and calculate profits in every day
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        for n in range(1, len(prices)):
            if(prices[n-1]<prices[n]):
                result += (prices[n]-prices[n-1])
        return result
            