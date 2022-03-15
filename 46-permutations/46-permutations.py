class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        def helper(index):
            if index == n:
                ans.append(nums[::])
                return
            
            for i in range(index,n):
                nums[i],nums[index] = nums[index],nums[i]
                helper(index+1)
                nums[i],nums[index] = nums[index],nums[i]
        
        helper(0)
        return ans