"""
    Date: 2021/11/09
    Key: Recursion
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def find_diameter(self, node, diameter):
        if(not node):
            return 0, diameter

        left, diameter = self.find_diameter(node.left, diameter)
        right, diameter = self.find_diameter(node.right, diameter)
        diameter = max(diameter, left+right)
        
        return 1 + max(left, right), diameter
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0
        temp = 0
        
        temp, max_diameter = self.find_diameter(root, max_diameter)
        return max_diameter
    
