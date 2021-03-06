"""
    Author: Weng Xiang Heng
    Date: 2021/10/30
    Key Point: Stack
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        stack = []
        
        stack.append(head)
        
        while(stack):
            if(not head):
                return False
            elif(not head.next):
                return False
            else:
                head = head.next
                if head in stack:
                    return True
                else:
                    stack.append(head)
        return False