#User function Template for python3

# class Solution:
#     def isSubsetSum (self, N, arr, sum):
#         # code here 
#         dp = [[False for i in range(sum+1)]for j in range(N+1)]

#         for i in range(N+1):
#             dp[i][0] = True
            
        
#         for i in range(1,N+1):
#             for j in range(1,sum+1):
#                 if j < arr[i-1]:
#                     dp[i][j] = dp[i-1][j]
                
#                 else :
#                     dp[i][j] = dp[i-1][j] or dp[i-1][j-arr[i-1]]
                    
#         return dp[N][sum]


class Solution:
    def isSubsetSum (self, N, arr, sum):
        # code here 
        dp = [[None for i in range(sum+1)]for j in range(N+1)]
        
        def helper(N,sum):     
            if N == 0:
                return sum == 0

            if sum == 0:
                return True
                
            if dp[N][sum] != None:
                return dp[N][sum]
            
            if arr[N-1] > sum:
                dp[N][sum] = helper(N-1,sum)
                return dp[N][sum]
                
            else :
                dp[N][sum] = helper(N-1,sum) or helper(N-1,sum-arr[N-1])
                return dp[N][sum]
                
        return helper(N,sum)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        for itr in range(N):
            arr[itr] = int(arr[itr])
        sum = int(input())

        ob = Solution()
        if ob.isSubsetSum(N,arr,sum)==True:
            print(1)
        else :
            print(0)
            
        

# } Driver Code Ends