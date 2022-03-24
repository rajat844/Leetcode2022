class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k
        
        def helper(l,r):
            pivot = nums[r]
            p = l
            
            for i in range(l,r):
                if nums[i] <= pivot:
                    nums[i],nums[p] = nums[p],nums[i]
                    p += 1
            
            nums[p],nums[r] = nums[r],nums[p]
            
            if p > k:
                return helper(l,p-1)
            elif p < k:
                return helper(p+1,r)
            if p == k:
                return nums[p]
        
        return helper(0,len(nums) - 1)