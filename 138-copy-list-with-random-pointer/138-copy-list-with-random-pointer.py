"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        while curr:
            nex = curr.next
            curr.next = Node(curr.val)
            curr.next.next = nex
            curr = nex
        
        curr = head
        while curr:
            if curr.random != None:
                curr.next.random = curr.random.next 
            curr = curr.next.next
            
        curr = head
        temp = ans = Node(0)
        
        while curr:
            temp.next = curr.next
            curr.next = curr.next.next
            curr = curr.next
            temp = temp.next
            
        return ans.next
            