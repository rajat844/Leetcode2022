class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        def findFloors(n,k):
            if dp[n][k] != -1:
                return dp[n][k]
            
            if n <= 1 or k <= 1:
                dp[n][k] = n
                return dp[n][k]
            
            ans = math.inf
            l = 1
            h = n
            
            while l <= h:
                mid = (l+h) >> 1
                left = findFloors(mid-1,k-1)
                right = findFloors(n-mid,k)
                temp = 1+max(left,right)
                if left < right:
                    l = mid + 1
                else:
                    h = mid - 1
                
                ans = min(ans,temp)                 
            dp[n][k] = ans
            return dp[n][k]
        
        dp = [[-1 for i in range(k+1)]for j in range(n+1)]
        return findFloors(n,k)
                