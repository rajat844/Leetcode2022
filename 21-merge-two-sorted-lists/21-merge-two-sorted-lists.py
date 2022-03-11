# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = temp = ListNode(0)
        while list1 and list2:
            if list1.val > list2.val:
                temp.next = list2
                temp = temp.next
                list2 = list2.next
            else:
                temp.next = list1
                temp = temp.next
                list1 = list1.next
                
        if list1 or list2:
            temp.next = list1 or list2 
            
        return head.next
        