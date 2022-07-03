# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, curr: Optional[ListNode]) -> Optional[ListNode]:
        if curr == None:
            return None
        head_odd  = temp_odd= ListNode(0)
        head_even = temp_even = ListNode(0)
        i = 1
        while curr:
            if i % 2 == 1:
                temp_odd.next = curr
                temp_odd = temp_odd.next
            else:
                temp_even.next = curr
                temp_even = temp_even.next
            curr = curr.next
            i += 1
        
        temp_odd.next = head_even.next
        temp_even.next = None
        return head_odd.next