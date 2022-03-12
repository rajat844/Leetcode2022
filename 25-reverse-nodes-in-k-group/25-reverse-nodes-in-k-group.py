# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count = 1
        curr = head
        while curr.next:
            curr = curr.next
            count += 1
        
        ans = prev = ListNode(0)
        curr = head
        nex = None
        prev.next = curr
        
        x = count//k
        for i in range(x):
            for j in range(k-1):
                nex = curr.next
                curr.next = nex.next
                nex.next = prev.next
                prev.next = nex
            prev = curr
            curr = curr.next
        
        return ans.next
            
        