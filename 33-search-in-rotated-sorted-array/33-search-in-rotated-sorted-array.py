class Solution:
    def search(self, nums: List[int], target: int) -> int:
        h = len(nums)-1
        l = 0
        m = 0
        while h>=l:
            m = (h+l)//2
            if nums[m] == target:
                return m
            elif nums[m] >= nums[l]:
                if target >= nums[l] and target <= nums[m]:
                    h = m-1
                else :
                    l = m+1
            else:
                if target >= nums[m] and target <= nums[h]:
                    l = m+1
                else:
                    h = m-1
            
        if nums[m] == target:
            return m
        else :    
            return -1
            
        
        