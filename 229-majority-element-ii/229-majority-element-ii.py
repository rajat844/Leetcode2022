import math
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ele1 = math.inf
        ele2 = math.inf
        count1 = 0
        count2 = 0
        
        for i in range(len(nums)):
            if nums[i] == ele1:
                count1 += 1
            elif nums[i] == ele2:
                count2 += 1
            elif count1 == 0:
                ele1 = nums[i]
                count1 += 1
            elif count2 == 0:
                ele2 = nums[i]
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
        
        x = 0
        y = 0
        for i in range(len(nums)):
            if nums[i] == ele1:
                x += 1
            if nums[i] == ele2 :
                y += 1
        ans = []
        if x > len(nums)//3:
            ans.append(ele1)
        if y > len(nums)//3:
            ans.append(ele2)
        
        return ans
            
            