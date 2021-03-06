"""
    Author: Weng Xiang Heng
    Date: 2021/10/26
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair = []
        before_ans = []
        
        for n, num in enumerate(nums):
            
            for n_n in range(len(before_ans)):
                if(before_ans[n_n][0] == num):
                    pair.append(before_ans[n_n][1]) 
                    pair.append(n)
                    
                    
            before_ans.append((target - num, n))
        return pair