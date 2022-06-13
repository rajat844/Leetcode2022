# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:    
    def sortedListToBST(self, node: Optional[ListNode]) -> Optional[TreeNode]:
        if node is None:
            return None
        if node.next is None:
            return TreeNode(node.val)
        slow = node
        fast = node
        prev = None
        
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
            
        prev.next = None
        node2 = slow.next
        slow.next = None
        
        root = TreeNode(slow.val)
        root.left = self.sortedListToBST(node)
        root.right = self.sortedListToBST(node2)
        return root