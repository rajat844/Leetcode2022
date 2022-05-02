# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        size = 0
        curr = head
        while curr:
            size += 1
            curr = curr.next
        
        m = size//k
        
        root = prev = ListNode(0)
        curr = head
        
        prev.next = curr
        
        for i in range(m):
            for j in range(k-1):
                nex = curr.next
                curr.next = nex.next
                nex.next = prev.next
                prev.next = nex
            
            prev = curr
            curr = curr.next
        
        return root.next