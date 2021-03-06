"""
    Author: Weng Xiang Heng
    Date: 2021/11/06
"""
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        dict_table = {}
        ans = []
        
        for num in nums:
            if(not num in dict_table):
                dict_table[num] = 0
            else:
                temp = dict_table.pop(num, None)
                
        for num in nums:
            if(num in dict_table):
                ans.append(num)
        
        return ans