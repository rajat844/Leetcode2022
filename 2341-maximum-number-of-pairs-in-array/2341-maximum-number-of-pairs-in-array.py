from collections import defaultdict
class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        st = defaultdict(int)
        for i in range(len(nums)):
            st[nums[i]] += 1
        
        ans = [0,0]
        
        for x in st:
            if st[x] % 2 != 0:
                ans[1] += 1
            ans[0] += st[x]//2
        return ans
        