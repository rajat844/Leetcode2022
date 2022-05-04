from collections import defaultdict
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        st = defaultdict(int)
        
        cntpairs = 0
        for i in range(len(nums)):
            if nums[i] in st:
                cntpairs += 1
                st[nums[i]] -= 1
                if st[nums[i]] == 0:
                    del st[nums[i]]
            else :
                st[k - nums[i]] += 1
                
        
        return cntpairs
            