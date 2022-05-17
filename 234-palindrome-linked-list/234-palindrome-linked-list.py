# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def reverse(node):
            curr = node
            prev = None
            while curr:
                nex = curr.next
                curr.next = prev
                prev = curr
                curr = nex
            return prev
        
        if head == None or head.next == None:
            return True
        slow = head
        fast = head 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        slow = reverse(slow)
        fast = head
        while slow:
            if slow.val != fast.val:
                return False
            slow = slow.next
            fast = fast.next
            
        return True