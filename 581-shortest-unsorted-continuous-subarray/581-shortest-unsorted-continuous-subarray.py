class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        end = -1
        mx = nums[0]
        
        for i in range(1,len(nums)):
            if mx > nums[i]:
                end = i
            else :
                mx = nums[i]
                
        st = 0
        mn = nums[-1]
        for i in range(len(nums) - 2, -1 ,-1):
            if mn < nums[i]:
                st = i
            else :
                mn = nums[i]
        
        return end - st + 1