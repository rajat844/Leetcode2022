# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root is None:
            return []
        def isLeaf(root):
            if root.left == None and root.right == None:
                return True
        
        def helper(root,arr,Sum):
            
            Sum = Sum + root.val
            arr.append(root.val)
            
            if isLeaf(root) == True:
                if Sum == targetSum:
                    x = []
                    for i in range(len(arr)):
                        x.append(arr[i])
                    ans.append(x)
            
            else :
                if root.left:
                    helper(root.left,arr,Sum)
                if root.right:
                    helper(root.right,arr,Sum)
            arr.pop()
            
        ans = []
        arr = []
        helper(root,arr,0)
        
        return ans
                
                
        