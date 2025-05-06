# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        asize = 0
        bsize = 0
        pointerA = headA
        pointerB = headB
        
        while pointerA:
            asize += 1
            pointerA = pointerA.next
        pointerA = headA
        
        while pointerB:
            bsize += 1
            pointerB = pointerB.next
        pointerB = headB
        
        while asize > bsize:
            pointerA = pointerA.next
            asize -= 1
        
        while asize < bsize:
            pointerB = pointerB.next
            bsize -= 1
        
        while pointerA is not pointerB:
            pointerA = pointerA.next
            pointerB = pointerB.next
        
        return pointerA

        
        

        
        