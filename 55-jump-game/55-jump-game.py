class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        
        prev = n-1        
        for i in range(n-2,-1,-1):
            x = nums[i]
            for j in range(1,x+1):
                if i+j >= prev:
                    prev = i
                    break
        
        if prev == 0:
            return True
        return False
        