#User function Template for python3
import math
class Solution:
    def canRepresentBST(self, nums, N):
        # code here
        st = []
        root = -math.inf
        
        for i in range(N):
            while len(st) > 0 and st[-1] < nums[i]:
                root = st.pop()
            
            if root > nums[i]:
                return 0
            st.append(nums[i])
        
        return 1

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        for itr in range(N):
            arr[itr] = int(arr[itr])
        
        ob = Solution()
        print(ob.canRepresentBST(arr, N))
# } Driver Code Ends