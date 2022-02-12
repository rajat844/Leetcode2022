class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = max(nums)
        
        currMax , currMin = 1,1
        
        for x in nums:
            if x == 0:
                currMax,currMin = 1,1
                continue
            mx = currMax
            my = currMin
            
            currMax = max(mx*x,my*x,x)
            currMin = min(mx*x,my*x,x)
            
            ans = max(currMax,ans)
        
        return ans
            
        