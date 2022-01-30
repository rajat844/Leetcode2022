class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(start,end):
            while start < end:
                x = nums[start]
                nums[start] = nums[end]
                nums[end] = x
                start += 1
                end -= 1
        k %= len(nums)     
        reverse(0,len(nums)-1)
        reverse(0,k-1)
        reverse(k,len(nums)-1)