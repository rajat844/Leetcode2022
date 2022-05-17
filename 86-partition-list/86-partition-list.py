# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        temp1 = left = ListNode(-101)
        temp2 = right = ListNode(-101)
        
        curr = head
        while curr:
            if curr.val < x:
                temp1.next = curr
                curr = curr.next
                temp1 = temp1.next
            else:
                temp2.next = curr
                curr = curr.next
                temp2 = temp2.next
        temp2.next = None       
        temp1.next = right.next
        return left.next