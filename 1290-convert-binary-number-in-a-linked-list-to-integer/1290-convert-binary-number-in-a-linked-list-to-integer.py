# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        size = 0
        curr = head
        while curr:
            size += 1
            curr = curr.next
        
        ans = 0
        curr = head
        for i in range(size):
            x = curr.val
            ans += x * (2 **(size - i -1))
            curr = curr.next
        
        return ans
            
        