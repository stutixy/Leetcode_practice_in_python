# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, s: str) -> Optional[TreeNode]:
        i = 0
        val = 0
        while i < len(s) and s[i] != '-':
            i += 1
        root = TreeNode(int(s[0:i]))
        stack = [root]
        count = 0

        while i < len(s):
            if s[i] == '-':
                count += 1
                i += 1
                continue
            j = i
            while i < len(s) and s[i] != '-':
                i += 1
            newNode = TreeNode(int(s[j:i]))
            while count < len(stack):
                stack.pop()
            count = 0
            node = stack[-1]
            if not node.left :
                node.left = newNode
            else:
                node.right = newNode
            stack.append(newNode)
            
        return root

                