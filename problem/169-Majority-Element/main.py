"""
    Author: Weng Xiang Heng
    Date: 2021/11/02
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict_table = {}
        ans = 0
        count = 0
        
        for num in nums:
            if(num in dict_table):
                dict_table[num] += 1
            else:
                dict_table[num] = 1
            if(dict_table[num] >= (len(nums)//2) and count < dict_table[num]):
                count = dict_table[num]
                ans = num
        return ans