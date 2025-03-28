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
        stack1 = [node1]
        stack2 = [node2]

        while len(stack1)>0 and len(stack2) > 0:
            current1 = stack1.pop()
            current2 = stack2.pop()
            
            if current1 and current2 and current1.val == current2.val:
                stack1.append(current1.right)
                stack2.append(current2.right)
                stack1.append(current1.left)
                stack2.append(current2.left)
 
            elif not current1 and not current2:
                continue
            else:
                return False
        return True




        


        


          
        
    



        