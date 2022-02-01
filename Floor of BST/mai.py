''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

    Following is the TreeNode class structure

    class TreeNode:

        def __init__ (self, data):

            self.data = data
            self.left = None
            self.right = None
            
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


def floorInBST(root, X):

    # Write your Code here.
    floor = -1
    while root is not None:
        if root.data == X:
            floor = root.data
            return floor
        if X > root.data:
            floor = root.data
            root = root.right
        else:
            root = root.left
    return floor

    '''
    Following is the TreeNode class structure

    class TreeNode:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None
'''
