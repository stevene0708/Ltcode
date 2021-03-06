"""
    Date:2021/10/28
"""
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        s = 0
        e = len(nums) - 1
        return self.search(nums, target, s, e)
    
    def search(self, nums: List[int], target: int, start , end):
        mid = (start + end) // 2
        
        if(start >= end):
            return start + (nums[start] < target)
        if(nums[mid] > target):
            return self.search(nums, target, start, mid-1)
        elif(nums[mid] < target):
            return self.search(nums, target, mid+1, end)
        else:
            return mid