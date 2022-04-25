class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = [1 for i in range(len(nums))]
        cnt = [1 for i in range(len(nums))]
        
        ans = 0
        mx = 0
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    cnt[i] = cnt[j]
                elif nums[i] > nums[j] and dp[i] == dp[j] + 1:
                    cnt[i] += cnt[j]
        
        
        mx = max(dp)
        
        for i in range(len(nums)):
            if dp[i] == mx:
                ans += cnt[i]
                
        return ans