# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        prev = None
        node = head

        while node:
            if node.val == val:
                if prev:
                    prev.next = node.next
                else:
                    head = head.next
            else:
                prev = node
            node = node.next
        return head
        