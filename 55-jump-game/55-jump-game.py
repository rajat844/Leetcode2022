class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        last = n-1
        
        for i in range(n-2,-1,-1):
            x = nums[i]
            if i+x >= last:
                last = i
                
        if last == 0:
            return True
        return False

                
                
        