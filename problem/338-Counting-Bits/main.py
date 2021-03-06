"""
    Author: Weng Xinag Heng
    Date: 2021/11/11
"""
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]
        
        for i in range(1, n+1):
            count = 0
            num = i
            while(num):
                if(num%2 == 1):
                    count += 1
                num = num//2
            ans.append(count)
            
        return ans