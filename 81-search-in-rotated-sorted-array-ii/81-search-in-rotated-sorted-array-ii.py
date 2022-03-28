class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        h = len(nums) - 1
        l = 0
        
        while l <= h:
            while l < h and nums[l] == nums[l+1]:
                l += 1
            while h > l and nums[h] == nums[h-1]:
                h -= 1
                
            mid = (l+h)//2
            
            if nums[mid] == target :
                return True
            
            elif nums[l] <= nums[mid]:
                if nums[mid] >= target and nums[l] <= target:
                    h = mid -1
                else :
                    l = mid + 1
            else :
                if nums[mid] <= target and target <= nums[h]:
                    l = mid + 1
                else :
                    h = mid - 1
        
        return False
        