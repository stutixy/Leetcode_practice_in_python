# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        height, isBalanced = self.postOrder(root, 0, True)
        return isBalanced
    
    def postOrder(self, current, height, isBalanced):
        if not current:
            return 0, True
        if not isBalanced:
            return height, isBalanced
        leftheight, isBalanced = self.postOrder(current.left, 0, isBalanced)
        if isBalanced:
            rightheight, isBalanced = self.postOrder(current.right, 0, isBalanced)
            if isBalanced:
                return max(leftheight, rightheight) + 1, abs(leftheight - rightheight) < 2
        return height, isBalanced


         
        