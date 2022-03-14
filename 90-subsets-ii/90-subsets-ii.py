class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        
        def helper(index,s):
            if index == len(nums):
                ans.append(s[::])
                return
            s.append(nums[index])
            helper(index + 1,s)
            s.pop()
            
            while index + 1 <len(nums) and nums[index] == nums[index+1]:
                index  += 1
            helper(index+1,s)
            
                
        helper(0,[])
        return ans