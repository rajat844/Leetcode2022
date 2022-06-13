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
        count = 1
        curr = head
        while curr and count != left:
            count += 1
            prev = curr
            curr = curr.next
        if count == left:
            for i in range(left,right):
                nex = curr.next
                curr.next = nex.next
                nex.next = prev.next
                prev.next = nex
        return dummy.next
            
        