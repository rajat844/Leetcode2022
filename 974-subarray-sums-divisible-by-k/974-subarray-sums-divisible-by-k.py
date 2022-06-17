from collections import defaultdict
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        st = defaultdict(int)
        s = 0
        ans = 0
        st[0] += 1
        
        for i in range(len(nums)):
            s += nums[i]
            rem = s%k
            if rem in st :
                ans += st[rem]
            st[rem] += 1
        
        return ans
            
            
        