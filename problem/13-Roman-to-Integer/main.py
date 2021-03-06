"""
    Author: Weng Xiang Heng
    Date: 2021/10/31
"""
class Solution:
    def romanToInt(self, s: str) -> int:
        dict_table = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        stack = []
        temp = 0
        sum_ = 0
        
        for str_ in s:
            if(stack):
                temp = stack.pop()
                stack.append(str_)
                if(dict_table[str_] > dict_table[temp]):
                    sum_ -= 2*dict_table[temp] - dict_table[str_]
                else:
                    sum_ += dict_table[str_] 
            else:
                stack.append(str_)
                sum_ += dict_table[str_] 
            
        return sum_
            
            
            