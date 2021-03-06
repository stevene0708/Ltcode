"""
    Author: Weng Xiang Heng
    Date: 2021/11/19
"""
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ans = x^y
        count = 0
        
        while(ans):
            if(ans % 2 == 1):
                count+=1
            ans = ans//2
        return count