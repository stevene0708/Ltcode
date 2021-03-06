"""
    Date: 2021/11/17
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 0
        max_ = 0
        dict_table = {}
        
        for num in range(len(s)):
            if(s[num] in dict_table and start <= dict_table[s[num]]):
                start = dict_table[s[num]]+1
            if(max_ < end-start+1):
                max_ = end-start+1
            
            dict_table[s[num]] = end
            end+=1
        return max_
        