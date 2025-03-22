class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        return self.buildTree(head, None)
         
    
    def buildTree(self, start, end):
        if start == end:
            return None
        fast = start
        slow = start
       
        while fast != end:
            fast = fast.next
            if fast != end:
                fast = fast.next
                slow = slow.next
        newNode = TreeNode(slow.val)
        newNode.left = self.buildTree(start, slow)
        newNode.right = self.buildTree(slow.next, end)
        return newNode        