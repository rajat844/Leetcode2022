class Solution:
    def find_height(self,tree,n,k):
        # code here
        def collect(x):
            temp = 0
            for i in range(n):
                if tree[i] > x:
                    temp += tree[i] - x
            
            return temp
        l = 0
        h = max(tree)
        
        while l <= h:
            mid = (l+h) >> 1
            
            collected = collect(mid)
            
            if collected == k:
                return mid
                
            elif collected > k:
                l = mid + 1
            else :
                h = mid - 1
        
        return - 1

#{ 
#  Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        tree = [ int(x) for x in input().strip().split() ]
        k = int(input())
        ob=Solution()
        print(ob.find_height(tree,n,k))
# } Driver Code Ends