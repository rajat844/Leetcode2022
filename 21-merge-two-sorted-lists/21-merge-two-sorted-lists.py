# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = value = ListNode(0)
        
        while list1 and list2 :
            if list2.val >= list1.val:
                value.next = list1
                list1 = list1.next
                value = value.next
            else :
                value.next = list2
                list2 = list2.next
                value = value.next
        value.next = list1 or list2
        return head.next
            
        
        