"""
    Author: Weng Xiang Heng
    Date: 2021/10/30
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        dict_ = {}
        
        value = 0
        dict_[head] = value
        
        while(dict_):
            if(not head):
                return False
            elif(not head.next):
                return False
            else:
                head = head.next
                if head in dict_:
                    return True
                else:
                    value+=1
                    dict_[head] = value
        return False