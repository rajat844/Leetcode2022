# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        st1 = []
        st2 = []
        while l1:
            st1.append(l1.val)
            l1 = l1.next
        while l2:
            st2.append(l2.val)
            l2 = l2.next
        
        carry = 0
        head = None
        while len(st1) > 0 and len(st2) > 0:
            x = carry + st1.pop() + st2.pop()
            carry = x // 10
            x = x % 10
            temp = ListNode(x)
            temp.next = head
            head = temp
        
        while len(st1) > 0:
            x = carry + st1.pop()
            carry = x // 10
            x = x % 10
            temp = ListNode(x)
            temp.next = head
            head = temp
        
        while len(st2) > 0:
            x = carry + st2.pop()
            carry = x // 10
            x = x % 10
            temp = ListNode(x)
            temp.next = head
            head = temp
        
        while carry > 0 :
            x = carry % 10
            carry = carry//10
            temp = ListNode(x)
            temp.next = head
            head = temp
        
        return head
            
            
        
            
        