class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        sortedArray = []
        node = head
        while node:
            sortedArray.append(node.val)
            node = node.next
        
        root = self.buildTree(sortedArray, 0, len(sortedArray)-1)
        return root
    
    def buildTree(self, arr, left, right):
        if left <= right:
            mid = int((left+right)/2)
            newNode = TreeNode(arr[mid]) 
            newNode.left = self.buildTree(arr,left,mid-1)
            newNode.right = self.buildTree(arr,mid+1,right)
            return newNode
        return None
            


        
        

        