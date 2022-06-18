from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        st = defaultdict(int)
        
        s,ans = 0,0
        st[s] += 1
        
        for i in range(len(nums)):
            s += nums[i]
            x = s - k
            if x in st:
                ans += st[x]
            st[s] += 1
        
        return ans
        