class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dic = {}
        maxcount = 0
        for i in range(len(nums)):
            dic[nums[i]] = i
        
        for i in range(len(nums)):
            if nums[i] - 1 in dic:
                continue
            else :
                count = 0
                x = nums[i]
                while x in dic:
                    count += 1
                    x += 1
                maxcount = max(count,maxcount)
        return maxcount  