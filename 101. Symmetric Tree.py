# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return None
        return self.traverse(root.left, root.right)

    def traverse(self, node1, node2):
        if node1 and node2:
            if node1.val == node2.val:
                if self.traverse(node1.left, node2.right):
                    return self.traverse(node1.right, node2.left)
                return False

        if node1 or node2:
            return False
        return True

        
        