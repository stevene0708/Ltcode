"""
    Author: Weng Xiang Heng
    Date: 2021/11/02
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        head_ = None      
        while(head):
            if(not stack):
                stack.append(ListNode(head.val))
                head = head.next
            else:
                temp = stack.pop()
                head_ = ListNode(head.val, temp)
                stack.append(head_)
                head = head.next
                
        if(stack):
            head_ = stack.pop()
            
        return head_
                
            