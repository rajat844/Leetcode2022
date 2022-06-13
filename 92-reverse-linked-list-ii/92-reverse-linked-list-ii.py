# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head == None or head.next == None or left == right:
            return head
        
        dummy = prev = ListNode(0)
        dummy.next = head
        
        for i in range(left-1):
            prev = head
            head = head.next
        
        for i in range(left,right):
            nex = head.next
            head.next = nex.next
            nex.next = prev.next
            prev.next = nex
        
        return dummy.next
            