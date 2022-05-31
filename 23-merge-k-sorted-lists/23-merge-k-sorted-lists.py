# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        n  = len(lists)
        i = n-1
        
        while i > 0:
            l1 = lists[i]
            l2 = lists[i-1]
            
            head = temp = ListNode(0)
            
            while l1 and l2 :
                if l1.val > l2.val:
                    temp.next = l2
                    l2 = l2.next
                    temp = temp.next
                else:
                    temp.next = l1
                    l1 = l1.next
                    temp = temp.next
            if l1 or l2:
                temp.next = l1 or l2
                
            lists[i-1] = head.next
            i -= 1
        
        return lists[0]
            
            
        