# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        li = []
        st = deque([root])
        while len(st) > 0:
            node = st.popleft()
            if node is None:
                li.append('')
            else :
                li.append(str(node.val))
                st.append(node.left)
                st.append(node.right)
        return ','.join(li)
    
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0:
            return None
        li = data.split(',')
        root = TreeNode(int(li[0]))
        q = deque([root])
        i = 1
        while len(q) > 0:
            node = q.popleft()
            if i < len(li) and li[i]:
                node.left = TreeNode(int(li[i]))
                q.append(node.left)
            i += 1
            if i< len(li) and li[i]:
                node.right = TreeNode(int(li[i]))
                q.append(node.right)
            i +=1
        return root
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))