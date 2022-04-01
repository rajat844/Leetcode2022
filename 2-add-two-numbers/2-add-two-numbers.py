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
            s = carry
            if l1:
                s += l1.val
                l1 = l1.next
            if l2 :
                s += l2.val
                l2 = l2.next
            
            x,y = divmod(s,10)
            carry = x
            temp.next = ListNode(y)
            temp = temp.next
        
        if carry != 0:
            temp.next = ListNode(carry)
            temp = temp.next
        
        return head.next
        