"""
    Author: Weng Xiang Heng
    Date: 2021/10/31
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        countA = 0
        countB = 0
        stack = []
        
        stack.append(headB)
        stack.append(headA)
        while(headA):
            countA+=1
            headA = headA.next
        headA = stack.pop()
        while(headB):
            countB+=1
            headB = headB.next
        headB = stack.pop()
        
        if(countA > countB):
            while(headA):
                if(countA > countB):
                    headA = headA.next
                    countB+=1
                else:
                    if(headA == headB):
                        return headA
                    else:
                        headA = headA.next
                        headB = headB.next
        else:
             while(headB):
                if(countA < countB):
                    headB = headB.next
                    countA+=1
                else:
                    if(headA == headB):
                        return headB
                    else:
                        headA = headA.next
                        headB = headB.next
        return None
                
