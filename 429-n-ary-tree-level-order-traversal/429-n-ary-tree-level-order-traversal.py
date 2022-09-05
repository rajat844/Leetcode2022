"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []
        st = deque()
        ans = []
        
        st.append(root)
        
        while len(st) > 0:
            tempans = []
            k = len(st)
            while k > 0:
                k -= 1
                node = st.popleft()
                tempans.append(node.val)
                if node.children:
                    for x in node.children:
                        st.append(x)
            
            ans.append(tempans)
        
        return ans
            
        