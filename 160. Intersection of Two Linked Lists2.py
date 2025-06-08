# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        sizeA = 0
        node = headA
        while node:
            sizeA += 1
            node = node.next

        sizeB = 0
        node = headB
        while node:
            sizeB += 1
            node = node.next
        
        diff = abs(sizeA-sizeB)

        one = headA if sizeA > sizeB else headB
        two = headA if sizeA <= sizeB else headB

        while diff:
            one = one.next
            diff -= 1
        
        while one and two:
            if one == two:
                return one
            one = one.next
            two = two.next
        return None


        
        

        
        