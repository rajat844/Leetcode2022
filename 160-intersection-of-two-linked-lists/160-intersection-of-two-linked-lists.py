# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        dummy1,dummy2 = headA,headB
        
        while dummy1 is not dummy2:
            dummy1 = headB if dummy1 is None else dummy1.next
            dummy2 = headA if dummy2 is None else dummy2.next        
        return dummy1