class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k
        
        def partition(start,end):
            i = start
            pivot = nums[end]
            
            for j in range(start,end):
                if nums[j] <= pivot:
                    nums[j],nums[i] = nums[i],nums[j]
                    i += 1
            nums[i],nums[end] = nums[end],nums[i]
            
            if i < k:
                return partition(i+1,end)
            elif i > k :
                return partition(start,i - 1)
            if i == k:
                return nums[i]
        
        return partition(0,len(nums) - 1)