"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return None
        
        curr = root
        
        while curr:
            dummy = Node(0)
            temp = dummy
            
            while curr:
                if curr.left:
                    temp.next = curr.left
                    temp = temp.next
                if curr.right:
                    temp.next = curr.right
                    temp = temp.next
                    
                curr = curr.next
            curr = dummy.next
                
        
        return root
        