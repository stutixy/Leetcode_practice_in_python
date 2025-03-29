# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.isEqualHelper(p, q)


    def isEqualHelper(self, node1, node2):
        if node1 and  node2:
            if node1.val != node2.val:
                return False
            isSame = True
            isSame = self.isEqualHelper(node1.left, node2.left)
            if isSame:
                isSame = self.isEqualHelper(node1.right, node2.right)
            return isSame
        elif node1 or node2:
            return False
        else:
            return True


        


          
        
    



        