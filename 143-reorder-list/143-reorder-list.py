# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def reverse(node):
            curr = node
            prev = None
            while curr:
                nex = curr.next
                curr.next = prev
                prev = curr
                curr = nex
            
            return prev
        
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        fast = slow.next
        slow.next = None
        fast = reverse(fast)
        slow = head
        
        while slow and fast:
            x = slow.next
            y = fast.next
            slow.next = fast
            fast.next = x
            slow = x
            fast = y
        