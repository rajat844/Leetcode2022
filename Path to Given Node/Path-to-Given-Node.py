# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):

        def helper(node,B):
            nonlocal arr
            if node is None:
                return False
            arr.append(node.val)
            if node.val == B or helper(node.left,B) or helper(node.right,B):
                return True
            
            arr.pop()
            return False
        
        arr = []
        if A is None:
            return arr
        
        helper(A,B)
        return arr
