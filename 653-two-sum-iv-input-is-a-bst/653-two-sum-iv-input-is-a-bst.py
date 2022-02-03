# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def next(self,root: Optional[TreeNode]):
        while root:
            self.ns.append(root)
            root = root.left
            
    def prev(self,root: Optional[TreeNode]):
        while root:
            self.ps.append(root)
            root = root.right
            
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        self.ns,self.ps = [],[]
        self.next(root)
        self.prev(root)
        
        while(len(self.ns) > 0 and len(self.ps) > 0  and self.ns[-1].val < self.ps[-1].val):
            if k == self.ns[-1].val + self.ps[-1].val:
                return True
            
            elif(k > self.ns[-1].val+ self.ps[-1].val):
                temp = self.ns.pop()
                self.next(temp.right)
            else:
                temp = self.ps.pop()
                self.prev(temp.left)
        
        return False