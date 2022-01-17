# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        dummy1,dummy2 = headA,headB
        
        while(dummy1 != dummy2):
            if dummy1: 
                dummy1 = dummy1.next 
            else :
                dummy1 = headB
            
            if dummy2 :
                dummy2 = dummy2.next
            else :
                dummy2 = headA
        
        return dummy1
        