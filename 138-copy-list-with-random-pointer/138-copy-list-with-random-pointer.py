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
            t = curr.next
            curr.next = Node(curr.val)
            curr.next.next = t
            curr = t
        
        curr = head
        while curr != None:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        
        curr = head
        temp = x = Node(0)
        
        while curr:
            t = curr.next
            temp.next = t
            temp = temp.next
            curr.next = curr.next.next
            curr = curr.next
            
        return x.next
            
        
        