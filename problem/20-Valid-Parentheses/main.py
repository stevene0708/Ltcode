"""
    Date: 2021/10/27
"""
class Solution:
    def isValid(self, s: str) -> bool:
        dict_ = {'(':')', '{':'}', '[':']'}
        stack = []
        
        for str_ in s:
            if(str_ in dict_):
                stack.append(str_)
            elif((not stack) or dict_[stack.pop()] != str_):
                return False
        
        return not stack
        
        