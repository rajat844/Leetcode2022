# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head :
            return None
        
        cnt = head
        
        for i in range(n):
            cnt = cnt.next
            
        if not cnt:
            return head.next
        
        crr = head
        while cnt.next:
            cnt = cnt.next
            crr = crr.next
        
        crr.next = crr.next.next

        return head
            