# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(i,j):
            if j < i:
                return None            
            else:
                mid = (i+j) >> 1
                
                node = TreeNode(nums[mid])
                node.left = helper(i,mid-1)
                node.right= helper(mid+1,j)
                
                return node
            
        return helper(0,len(nums) - 1)
                
                