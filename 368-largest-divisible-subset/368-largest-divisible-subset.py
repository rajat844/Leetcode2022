class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)        
        dp = [1 for i in range(n)]
        h = [i for i in range(n)] 
        lst = -1
        mx = 0
        
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    h[i] = j
                    
            if mx < dp[i]:
                mx = dp[i]
                lst = i
                
        ans = []
        while lst != h[lst]:
            ans.append(nums[lst])
            lst = h[lst]
        
        ans.append(nums[lst])
        ans.reverse()
        
        return ans
                