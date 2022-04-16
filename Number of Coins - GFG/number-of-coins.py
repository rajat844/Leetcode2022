#User function Template for python3
import math
class Solution:
	def minCoins(self, coins, M, V):
		# code 
		coins.sort
		dp = [math.inf for i in range(V + 1)]
		
		dp[0] = 0
		
		for i in range(1,V + 1):
		    for j in range(M):
		        if i >= coins[j] and dp[i-coins[j]] != math.inf and dp[i] > dp[i - coins[j]] + 1:
		            dp[i] = dp[i - coins[j]] + 1
		            
		if dp[V] == math.inf:
		    return -1
		
		return dp[V]
		
		        
		
		

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		v,m = input().split()
		v,m = int(v), int(m)
		coins = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minCoins(coins,m,v)
		print(ans)

# } Driver Code Ends