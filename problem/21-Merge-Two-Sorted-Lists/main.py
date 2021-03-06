"""
    Author: Weng Xiang Heng
    Date: 2021/10/31
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if(not l2):
            return l1
        elif(not l1):
            return l2
        else:
            if(l1.val < l2.val):
                l1.next = self.mergeTwoLists(l1.next, l2)
                return l1
            if(l1.val >= l2.val):
                temp = ListNode(l2.val, l1)
                l1 = temp
                l1.next = self.mergeTwoLists(l1.next, l2.next)
                return l1