# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head

        while fast and slow:
            fast = fast.next
            if fast:
                fast = fast.next
                slow = slow.next
            if fast and slow and fast == slow:
                return True
            
        return False


        