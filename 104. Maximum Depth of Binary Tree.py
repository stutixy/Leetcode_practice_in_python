# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        result = self.calculateMaxDepth(root, 0, 0)
        return result

    def calculateMaxDepth(self, currentNode, maxDepth, currentDepth):
        currentDepth += 1
        if currentNode.left == None and currentNode.right == None:
            if maxDepth < currentDepth:
                maxDepth = currentDepth
        if currentNode.left != None:
            leftMaxDepth = self.calculateMaxDepth(currentNode.left, maxDepth, currentDepth)
            if maxDepth < leftMaxDepth:
                maxDepth = leftMaxDepth
        if currentNode.right != None:
            rightMaxDepth = self.calculateMaxDepth(currentNode.right, maxDepth, currentDepth)
            if maxDepth < rightMaxDepth:
                maxDepth = rightMaxDepth
        
        return maxDepth

