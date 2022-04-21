class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st = {}
        n = len(nums)
        for i in range(n):
            st[nums[i]] = i
        
        count = 0
        for i in range(n):
            if nums[i] - 1 not in st:
                x = nums[i]
                tempcount = 0
                while x in st:
                    x += 1
                    tempcount += 1
                
                count = max(tempcount,count)
        
        return count
                     
                    
                        
                
        