import math
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = math.inf
        for i in range(len(nums)-2):
            l = i+1
            h = len(nums) - 1
            while l < h:
                x = nums[i] + nums[l] + nums[h] 
                if abs(x - target) < abs(target - closest):
                    closest = x
                    if closest == target:
                        return closest
                if x > target:
                    h -= 1
                else :
                    l += 1
        
        return closest
        
            
            
        