"""
    Author: Weng Xiang Heng
    Date: 2021/11/03
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        head_ = head
        
        while(head_):
            stack.append(head_.val)
            head_ = head_.next
            
        while(stack):
            head_t = stack.pop()
            if(head.val != head_t):
                return False
            head = head.next
            
        return True