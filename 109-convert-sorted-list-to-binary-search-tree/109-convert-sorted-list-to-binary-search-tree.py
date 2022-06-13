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
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def helper(node):
            if node == None:
                return None
            if node.next == None:
                return TreeNode(node.val)
            fast = node
            slow = node
            prev = None
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            
            prev.next = None           
            node2 = slow.next
            slow.next = None
            
            root = TreeNode(slow.val)
            root.left = helper(node)
            root.right = helper(node2)
            return root
        return helper(head)
            
                