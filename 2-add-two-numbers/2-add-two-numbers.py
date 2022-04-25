# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = temp = ListNode(0)
        carry = 0
        while l1 and l2:
            x = l1.val + l2.val + carry
            carry,sm= divmod(x,10)
            temp.next = ListNode(sm)
            temp = temp.next
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            x = l1.val + carry
            carry,sm= divmod(x,10)
            temp.next = ListNode(sm)
            temp = temp.next
            l1 = l1.next
        
        while l2 :
            x = l2.val + carry
            carry,sm= divmod(x,10)
            temp.next = ListNode(sm)
            temp = temp.next
            l2 = l2.next
        
        if carry:
            temp.next = ListNode(carry)
        
        return head.next
        
        
        