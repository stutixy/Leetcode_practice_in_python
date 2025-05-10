# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        prev = head
        fast = head
        while fast and n:
            fast = fast.next
            n -= 1
        while fast:
            fast = fast.next
            prev = slow
            slow = slow.next
        if prev is not slow:
            prev.next = slow.next
        else:
            head = head.next
        return head
    

        