# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = root = ListNode(-101)
        curr = head
        while curr:
            if curr.val == prev.val:
                curr = curr.next
            else:
                prev.next = curr
                curr = curr.next
                prev = prev.next
        
        prev.next = None
        return root.next
        