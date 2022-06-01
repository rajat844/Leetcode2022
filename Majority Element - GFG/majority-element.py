#User function template for Python 3

class Solution:
    def majorityElement(self, A, N):
        #Your code here
        ans = None
        cnt = 0
        
        for i in range(N):
            if cnt == 0:
                ans = A[i]
                cnt += 1
            elif A[i] == ans:
                cnt += 1
            else :
                cnt -= 1
        cnt = 0
        for i in range(N):
            if A[i] == ans:
                cnt += 1
        if cnt > N//2:
            return ans
        return -1
            

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

from sys import stdin


def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=[int(x) for x in input().strip().split()]
            
            
            obj = Solution()
            print(obj.majorityElement(A,N))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends