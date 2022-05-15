from collections import defaultdict
class Solution:
    def largestCombination(self, nums: List[int]) -> int:
        ans = 0
        for bit in range(32):
            cnt = 0
            for i in range(len(nums)):
                if nums[i] & (1 << (31 - bit)) == 0:
                    continue
                cnt += 1
                
            ans = max(cnt,ans)
        return ans