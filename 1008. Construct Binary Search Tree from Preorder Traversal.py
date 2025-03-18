# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        return self.buildTree(preorder, 0, len(preorder)-1)

    def buildTree(self, arr, start, end):
        if start < end:
            node = TreeNode(arr[start])
            pointer = start
            while pointer <= end:
                if arr[pointer] > arr[start]:
                    break
                pointer += 1
            node.left = self.buildTree(arr, start+1, pointer-1)
            node.right = self.buildTree(arr, pointer, end)
            return node
        elif start == end:
            return TreeNode(arr[start])


        return None
        