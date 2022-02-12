class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dic = {}
        
        for i in nums:
            if not i in dic:
                dic[i] = 1
            else :
                dic[i] += 1
        
        max_count = 0
            
        for i in range(len(nums)):
            if nums[i]-1 not in dic:
                count = 0
                x = nums[i]
                while x in dic:
                    x += 1
                    count += 1
                
                max_count = max(count,max_count)
        
        return max_count
        