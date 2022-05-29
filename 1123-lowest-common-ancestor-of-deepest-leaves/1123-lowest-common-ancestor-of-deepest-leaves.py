# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def findLca(node,deepest):
            if node is None:
                return None
            lh = findLca(node.left,deepest)
            rh = findLca(node.right,deepest)
            
            if node in deepest or lh and rh:
                return node
            elif lh or rh:
                return lh or rh
            else:
                return None
            
        st = []
        st.append(root)
        prev = []
        
        while len(st) > 0:
            prev = st[::]
            st = []
            for i in range(len(prev)):
                node = prev[i]
                if node.left:
                    st.append(node.left)
                if node.right:
                    st.append(node.right)
        
        deepest = set(prev)
        return findLca(root,deepest)
        
        
        