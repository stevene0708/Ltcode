"""
    Author: Weng Xiang Heng
    Date: 2021/11/05
    Key point: Brute force
"""
class Solution:
    def arrangeCoins(self, n: int) -> int:
        height = 0
        sum_ = 0
        
        for i in range(n):
            sum_ += (i+1)
            if(sum_ <= n):
                height += 1
            else:
                break
        return height
                