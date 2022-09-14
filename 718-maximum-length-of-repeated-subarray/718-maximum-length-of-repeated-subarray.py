class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[0 for i in range(len(nums1)+1)]for j in range(len(nums2)+1)]
        
        for i in range(1,len(nums2)+1):
            for j in range(1,len(nums1)+1):
                if nums2[i-1] == nums1[j-1]:
                    dp[i][j] = 1+dp[i-1][j-1]
                else:
                    dp[i][j] = 0
                    
        ans = 0
        for i in range(len(dp)):
            ans = max(ans,max(dp[i]))
            
        return ans