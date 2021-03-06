"""
    Author: Weng Xiang Heng
    Date: 2021/10/27
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dict_ = {}
        
        for num in nums:
            if(not num in dict_):
                dict_[num] = 1
            else:
                dict_[num] += 1
                
        for num in nums:
            if(dict_[num] <= 1):
                return num
                
                