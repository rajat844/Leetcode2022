# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None:
            return head
        curr = head
        count = 1
        while curr.next:
            curr = curr.next
            count += 1
        
        curr.next = head
        
        curr = head
        k = k%count
        rot = count - k
        
        for i in range(rot-1):
            head = head.next
            
        x = head
        head = head.next
        x.next = None
        
        return head
            