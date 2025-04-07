# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        def dfs(root):
            if not root:
                return (float('-inf'), 0) 
            
            longestPathSumInLeft, maxLeftHeightSum  = dfs(root.left)
            longestPathSumInRight, maxRightHeightSum  = dfs(root.right)
            longestPathSum = max(longestPathSumInLeft, longestPathSumInRight, maxLeftHeightSum + maxRightHeightSum + root.val, root.val)
            maxHeightSum = max(maxLeftHeightSum + root.val, maxRightHeightSum + root.val, root.val)
            longestPathSum = max(maxHeightSum, longestPathSum)
            return (longestPathSum, maxHeightSum)
        return dfs(root)[0]

        