# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        currentList = [root]
        res = []
        currentRes = []
        childrenQueue = []
        
        while True:
            while currentList:
                currentNode = currentList.pop(0)
                currentRes.append(currentNode.val)
                if currentNode.left:
                    childrenQueue.append(currentNode.left)
                if currentNode.right:
                    childrenQueue.append(currentNode.right)
            res.append(currentRes.copy())
            
            if childrenQueue:
                currentList = childrenQueue.copy()
                currentRes.clear()
                childrenQueue.clear()
            else:
                break
        return res





            
