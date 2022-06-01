#User function Template for python3

class Solution:
    def findNth(self,N):
        #code here
        ans = 0
        temp = 1
        while N:
            ans = ans + temp*(N%9)
            temp *= 10
            N = N//9
            
        return ans
            

#{ 
#  Driver Code Starts
#Initial Template for Python 3

t=int(input())
for i in range(0,t):
    n=int(input())
    obj=Solution()
    s=obj.findNth(n)
    print(s)
# } Driver Code Ends