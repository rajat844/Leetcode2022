#User function Template for python3
from collections import defaultdict
class Solution:
    def getPairsCount(self, arr, n, k):
        # code here
        st = defaultdict(int)
        
        ans = 0
        for i in range(n):
            if arr[i] in st:
                ans += st[arr[i]]
            st[k - arr[i]] += 1
        
        return ans
                

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getPairsCount(arr, n, k)
        print(ans)
        tc -= 1

# } Driver Code Ends