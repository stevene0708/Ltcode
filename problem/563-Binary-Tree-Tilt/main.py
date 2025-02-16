# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.sum = 0

        def dfs(node):
            if(not node):
                return 0
            sum_l = dfs(node.left)
            sum_r = dfs(node.right)
            self.sum += abs(sum_l - sum_r)
            return node.val + sum_l + sum_r
        dfs(root)
        return self.sum