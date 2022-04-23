class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def helper(i):
            if i == len(nums):
                ans.append(nums[::])
                return
            else:
                for x in range(i,n):
                    nums[x],nums[i] = nums[i],nums[x]
                    helper(i+1)
                    nums[i],nums[x] = nums[x],nums[i]
                        
        n = len(nums)
        ans = []
        helper(0)
        return ans