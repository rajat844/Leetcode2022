class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def helper(ind):
            if ind == len(nums):
                t = []
                for i in nums:
                    t.append(i)
                ans.append(t)
                return 
            for i in range(ind,len(nums)):
                nums[ind],nums[i] = nums[i],nums[ind]
                helper(ind+1)
                nums[ind],nums[i] = nums[i],nums[ind]        
            
        helper(0)
        return ans
        
        