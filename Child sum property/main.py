'''

    Following is the Binary Tree node structure
    
    class BinaryTreeNode:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

'''
        
def changeTree(root): 
    # Write your code here.
    if root is None:
        return 
    
    child = 0
    if root.left:
        child += root.left.data
    if root.right:
        child += root.right.data
    
    if child >= root.data:
        root.data = child
    else :
        if root.left:
            root.left.data = root.data
        if root.right:
            root.right.data = root.data
            
    changeTree(root.left)
    changeTree(root.right)
    
    total = 0
    if root.left:
        total += root.left.data
    if root.right:
        total += root.right.data
    if root.right or root.left:
        root.data = total
    pass