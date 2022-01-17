# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if head is None or k < 2:
            return head

        dummy = ListNode(0)
        dummy.next = head
        pre = cur = pos = dummy
        count = 0
        while(cur.next):
            count += 1
            cur = cur.next

        while count >= k:
            cur = pre.next
            pos = cur.next
            for i in range(k-1):
                cur.next = pos.next
                pos.next = pre.next
                pre.next = pos
                pos = cur.next
            pre = cur
            count -= k

        return dummy.next
                
                
                
                
            
                