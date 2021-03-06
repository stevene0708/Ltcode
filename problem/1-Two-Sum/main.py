"""
    Author: Weng Xiang Heng
    Date: 2021/10/27
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_ = {}

        for n in range(len(nums)):
            diff = target - nums[n]

            if nums[n] in dict_:
                return [dict_[nums[n]], n]
            else: 
                dict_[diff] = n