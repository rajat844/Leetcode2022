import math
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ele1 = math.inf
        ele2 = math.inf
        count1 = 0
        count2 = 0
        
        for i in range(len(nums)):
           
            if ele1 == nums[i]:
                count1  += 1
            
            elif ele2 == nums[i]:
                count2 += 1
                
            elif count1 == 0:
                count1 += 1
                ele1 = nums[i]
            
            elif count2 == 0:
                count2 += 1
                ele2 = nums[i]
                
            else:
                count1 -= 1
                count2 -= 1
        
        ans = []
        x = 0
        y = 0
        for i in range(len(nums)):
            if ele1 == nums[i]:
                x += 1
            elif ele2 == nums[i]:
                y += 1
        
        if x > len(nums)//3:
            ans.append(ele1)
        if y > len(nums)//3:
            ans.append(ele2)
            
        return ans
            
                