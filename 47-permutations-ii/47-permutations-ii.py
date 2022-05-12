class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def helper(s,nums):
            if not nums:
                ans.append(s[::])
            
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                helper(s +[ nums[i]],nums[:i] + nums[i+1:])
            
            
        nums.sort()
        ans = []
        helper([],nums)
        
        return ans