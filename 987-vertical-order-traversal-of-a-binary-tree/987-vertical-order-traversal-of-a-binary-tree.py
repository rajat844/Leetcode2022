# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        st = defaultdict(lambda:defaultdict(list))
        
        def helper(node,i,j):
            if node is None:
                return 
            
            st[i][j].append(node.val)
                
            helper(node.left,i-1,j+1)
            helper(node.right,i+1,j+1)
        helper(root,0,0)  
        
        ans = []
        for i in sorted(st):
            temp = []
            for j in sorted(st[i]):
                for k in sorted(st[i][j]):
                    temp.append(k)
            ans.append(temp)   
        return ans