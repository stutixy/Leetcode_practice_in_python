# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        pointer1 = l1
        pointer2 = l2
        prev = l1
        while pointer1 and pointer2:
           pointer1.val += pointer2.val
           pointer1.val += carry
           carry = int(pointer1.val/10)
           pointer1.val %= 10
           prev = pointer1
           pointer1 = pointer1.next 
           pointer2 = pointer2.next 
        
        if pointer2:
            prev.next = pointer2
            pointer1 = prev.next

        while pointer1 :
            pointer1.val += carry
            carry = int(pointer1.val/10)
            pointer1.val %= 10
            prev = pointer1
            pointer1 = pointer1.next
        
        if carry > 0:
            prev.next = ListNode(carry)
        return l1
           
           

        