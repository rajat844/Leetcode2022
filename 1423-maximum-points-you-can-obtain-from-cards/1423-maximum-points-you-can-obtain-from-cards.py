class Solution:
    def maxScore(self, nums: List[int], k: int) -> int:
        minsum = sum(nums)
        window = len(nums) - k
        r = -1
        s = 0
        for l in range(len(nums)):
            s += nums[l]
            while l-r > window:
                r += 1
                s -= nums[r]
            if l-r == window:
                minsum = min(minsum,s)
        
        return sum(nums) - minsum
        
        