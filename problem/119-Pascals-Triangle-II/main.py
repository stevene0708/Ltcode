"""
    Date: 2021/11/09
"""
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        dp = []
        for i in range(rowIndex+1):
            dp1 = []
            for j in range(i+1):
                dp1.append(1)
            dp.append(dp1)
            
        for n in range(2, rowIndex+1):
            for m in range(1, len(dp[n-1])):
                dp[n][m] = dp[n-1][m-1] + dp[n-1][m]
                
        return dp[rowIndex]
                