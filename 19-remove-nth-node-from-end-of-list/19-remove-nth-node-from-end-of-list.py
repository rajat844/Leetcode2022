# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head :
            return None
        
        curr = curr2 = head
        
        for i in range(n):
            curr = curr.next
        
        if not curr:
            return head.next
        
        while curr.next:
            curr = curr.next
            curr2 = curr2.next
        
        curr2.next = curr2.next.next
        
        return head
        
        
            
            
        
        