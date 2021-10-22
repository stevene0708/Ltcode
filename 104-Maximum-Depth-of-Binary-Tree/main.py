"""
    Author: Weng Xiang Heng
    Date: 2021/10/21
"""

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = []
        
        if(root == None):
            return 0
        else:
            top = root
            max_depth = 0
            depth = 0
            
            while(stack or top):
                while(top):
                    stack.append((top, depth+1))
                    top = top.left
                    depth+=1
                    
                L, depth = stack.pop()
                max_depth = max(max_depth, depth)
                top = L.right
                
        return max_depth