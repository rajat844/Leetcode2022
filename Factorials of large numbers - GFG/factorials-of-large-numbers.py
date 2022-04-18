#User function Template for python3

class Solution:
    
    def factorial(self, N):
        #code here
        ans = [1]
        carry = 0
        for i in range(2,N+1):
            for j in range(len(ans)):
                carry,ans[j]= divmod(i * ans[j] + carry,10)
            if carry != 0:
                ans.append(carry)
                carry = 0
        
        
        ans.reverse()
        return ans
                


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.factorial(N);
        for i in ans:
            print(i,end="")
        print()
    
# } Driver Code Ends