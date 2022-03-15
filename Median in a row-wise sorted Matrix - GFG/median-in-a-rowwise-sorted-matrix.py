#User function Template for python3
import math
class Solution:
    def median(self,A , r, c):
    	#code here 

        def num(x):
            ans = 0
            for i in range(n):
                l = 0
                h = m-1
                while l <= h:
                    mid = (l+h)//2
                    if A[i][mid] <= x:
                        l = mid+1
                    else :
                        h = mid -1
                ans += l
            return ans


        l = 1
        h = 2000
        

        n = len(A)
        m = len(A[0])
        
        while l <= h:
            mid = (l+h)//2
            if num(mid) <= (n*m)//2:
                l = mid+1
            else:
                h = mid-1
        return l

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        r,c = map(int,input().strip().split())
        matrix = [[0 for j in range(c)] for i in range(r)]
        line1 = [int(x) for x in input().strip().split()]       
        k = 0
        for i in range(r):
            for j in range (c):
                matrix[i][j]=line1[k]
                k+=1
        ans = ob.median(matrix, r, c);
        print(ans)
# } Driver Code Ends