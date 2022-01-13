# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev_node = None
        curr_node = head
        nex_node = None
        
        while curr_node :
            nex_node = curr_node.next
    
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = nex_node
        
        return prev_node
        