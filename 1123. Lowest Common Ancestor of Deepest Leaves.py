# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(root, depth, maxDepth):
            if not root:
                return (None, depth, maxDepth)

            leftlca, leftdepth, maxDepth = dfs(root.left, depth+1, maxDepth)
            rightlca, rightdepth, maxDepth = dfs(root.right, depth+1, maxDepth)

            if leftlca and rightlca:
                if leftdepth == rightdepth and leftdepth >= maxDepth:
                    return (root, leftdepth, leftdepth)
                if leftdepth > rightdepth and leftdepth >= maxDepth:
                    return (leftlca, leftdepth, leftdepth)
                if rightdepth >= maxDepth:
                    return (rightlca, rightdepth, rightdepth)
                return (None, max(leftdepth, rightdepth), maxDepth)
            
            if leftlca or rightlca:
                if leftlca and leftdepth >= maxDepth:
                    return (leftlca, leftdepth, leftdepth)
                if rightlca and rightdepth >= maxDepth:
                    return (rightlca, rightdepth, rightdepth)
                return (None, max(leftdepth, rightdepth), maxDepth)
            
            if depth >= maxDepth:
                return (root, depth, depth)
            return (None, depth,maxDepth) 

        return dfs(root, 0, -1)[0]

            
                
           


            
            


    
        