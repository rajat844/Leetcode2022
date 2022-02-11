# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = temp = ListNode(0)
        
        while l1 or l2:
            l1sum , l2sum = 0,0
            if l1 :
                l1sum = l1.val
                l1 = l1.next
            if l2 :
                l2sum = l2.val
                l2 = l2.next
            
            currsum = l1sum + l2sum + carry
            carry,x = divmod(currsum,10)
            temp.next = ListNode(x)
            temp = temp.next
            
        if carry != 0:
            temp.next = ListNode(carry)
            temp = temp.next
        
        return head.next
                