"""
    Author: Weng Xiang Heng
    Date: 2021/11/12
"""
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        c = 0
        if(not s):
            return True
        elif(not t):
            return False
        
        for n in range(len(t)):
            if(c < len(s)):
                if(s[c] == t[n]):
                    c+=1
        if(c==len(s)):
            return True
        else:
            return False