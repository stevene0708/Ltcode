"""
    Author: Weng Xiang Heng
    Date: 2021/10/26
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if(not root):
            return None
        else:
            tempL = self.invertTree(root.left)
            root.left = self.invertTree(root.right)
            root.right = tempL
            return root
            