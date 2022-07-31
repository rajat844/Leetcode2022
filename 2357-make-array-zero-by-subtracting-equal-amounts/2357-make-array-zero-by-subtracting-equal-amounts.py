class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        heapq.heapify(nums)
        ans = 0 
        while len(nums) > 0:
            while len(nums) > 0 and nums[0] == 0:
                heapq.heappop(nums)
            if len(nums) == 0:
                return ans
            ans += 1
            x = heapq.heappop(nums)
            for i in range(len(nums)):
                nums[i] -= x
        
        return ans