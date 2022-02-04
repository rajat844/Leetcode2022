#User function Template for python3

''' structure of tree node:

class Node:
    def __init__(self,x):
        self.data=x
        self.left=None
        self.right=None
        self.height=1

'''

class Solution:
    
    def getHeight(self,root):
        if not root:
            return 0
        return root.height
        
    def balanced(self,root):
        return self.getHeight(root.left)- self.getHeight(root.right)
    
    def LLRotation(self,a):
        b = a.left
        br = b.right
        
        b.right = a
        a.left = br
        
        a.height = 1 + max(self.getHeight(a.left),self.getHeight(a.right))
        b.height = 1 + max(self.getHeight(b.left),self.getHeight(b.right))
        
        return b
        
    def RRRotation(self,a):
        b = a.right
        bl = b.left
        
        b.left = a
        a.right = bl
        
        a.height = 1 + max(self.getHeight(a.left),self.getHeight(a.right))
        b.height = 1 + max(self.getHeight(b.left),self.getHeight(b.right))
        
        return b
        
    def LRRotation(self,a):
        b = a.left
        c = b.right
        cl = c.left
        cr = c.right

        c.right = a
        c.left = b
        a.left = cr
        b.right = cl
        
        a.height = 1 + max(self.getHeight(a.left),self.getHeight(a.right))
        b.height = 1 + max(self.getHeight(b.left),self.getHeight(b.right))
        c.height = 1 + max(self.getHeight(c.left),self.getHeight(c.right))

        return c

    def RLRotation(self,a):
        b = a.right
        c = b.left
        cl = c.left
        cr = c.right

        c.left = a
        c.right = b
        b.left = cr
        a.right = cl
        
        
        a.height = 1 + max(self.getHeight(a.left),self.getHeight(a.right))
        b.height = 1 + max(self.getHeight(b.left),self.getHeight(b.right))
        c.height = 1 + max(self.getHeight(c.left),self.getHeight(c.right))
        
        return c
    def insertToAVL(self, root, key):
        # add key to AVL (if it is not present already)
        # return root node
        
        if not root:
            return Node(key)
            
        if root.data > key:
            root.left = self.insertToAVL(root.left,key)
        elif root.data < key :
            root.right = self.insertToAVL(root.right,key)
            
        root.height = 1+max(self.getHeight(root.left),self.getHeight(root.right))
        
        if self.balanced(root) == 2 and self.balanced(root.left) == 1:
            root = self.LLRotation(root)
        elif self.balanced(root) == 2 and self.balanced(root.left) == -1:
            root = self.LRRotation(root)
        elif self.balanced(root) == -2 and self.balanced(root.right) == 1:
            root = self.RLRotation(root)
        elif self.balanced(root) == -2 and self.balanced(root.right) == -1:
            root = self.RRRotation(root)
        
        return root
#{ 
#  Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self,x):
        self.data=x
        self.left=None
        self.right=None
        self.height=1

def isBST(n, lower, upper):
    if not n:
        return True
    
    if n.data <= lower or n.data >= upper:
        return False
    
    return isBST(n.left, lower, n.data) and isBST(n.right, n.data, upper)

def isBalanced(n):
    if not n:
        return (0,True)
    
    lHeight, l = isBalanced(n.left)
    rHeight, r = isBalanced(n.right)
    
    if abs( lHeight - rHeight ) > 1:
        return (0, False)
    
    return ( 1 + max( lHeight,rHeight  ) , l and r )

def isBalancedBST(root):
    if not isBST(root, -1000000000, 1000000000):
        print("BST voilated, inorder traversal :", end=' ')
    
    elif not isBalanced(root)[1]:
        print("Unbalanced BST, inorder traversal :", end=' ')
    
    else:
        return True
    
    return False

def printInorder(n):
    if not n:
        return
    printInorder(n.left)
    print(n.data, end=' ')
    printInorder(n.right)

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        ip = [ int(x) for x in input().strip().split() ]
        
        root = None
        
        for i in range(n):
            root = Solution().insertToAVL( root, ip[i] )
            
            if not isBalancedBST( root ):
                break
        
        printInorder(root)
        print()

# } Driver Code Ends