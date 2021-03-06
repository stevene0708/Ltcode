"""
    Author: Weng Xiang Heng
    Date: 2021/11/12
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if(not head):
            return None

        if(head.val == val):
            head = head.next
            head = self.removeElements(head, val)
        else:
            head.next = self.removeElements(head.next, val)
            
        return head