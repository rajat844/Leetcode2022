#User function Template for python3

class Solution:
    def canReach(self, A, N):
        # code here
        # def jumps(i):
        #     if i == N-1:
        #         return True
            
        #     x = A[i]
        #     if x == 0:
        #         return False
        #     for j in range(i+1,i+x+1):
        #         if jumps(j) == True:
        #             return True
                
        #     return False 
        
        # return jumps(0)
        
        dp = [None for i in range(N)]
        
        dp[N-1] = True
        
        for i in range(N-2,-1,-1):
            x = A[i]
            if x == 0:
                dp[i] = False
            else:
                for j in range(i+1,i+x+1):
                    if dp[j] == True:
                        dp[i] = True
                        break
                    else:
                        dp[i] = False
        if dp[0] ==False:
            return 0
        else :
            return 1
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        A=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.canReach(A,N))
# } Driver Code Ends