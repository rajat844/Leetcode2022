class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        mid = len(nums) // 2
        nums.sort()
        
        ans = 0
        for i in range(len(nums)):
            ans += abs(nums[i] - nums[mid])
        
        return ans