# Definition for a binary tree node.
# class TreeNode:
    # def __init__(self, val=0, left=None, right=None):
    #     self.val = val
    #     self.left = left
    #     self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(node, sumV):
            if not node:
                return False
            sumV += node.val
            if not node.left and not node.right:
                return sumV == targetSum 
            if node.left and dfs(node.left, sumV):
                return True
            if node.right and dfs(node.right, sumV):
                return True
            
            return False
            
        return dfs(root, 0)
            
