"""
    Author: Weng Xiang Heng
    Date: 2022/02/05
    Key point: Dictionary
"""
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        dict_t = {}
        ans = []
        
        for i in range(1, len(nums)+1):
            dict_t[i] = 0
        
        for j in nums:
            if (j in dict_t):
                dict_t[j] += 1
                
        for k in range(1, len(nums)+1):
            if(dict_t[k] == 0):
                ans.append(k)
        
        return ans
                