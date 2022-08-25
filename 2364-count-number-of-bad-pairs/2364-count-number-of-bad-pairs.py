class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        ans = 0
        st = defaultdict(int)
        
        for i in range(len(nums)):
            ans += i - st[nums[i] - i]
            st[nums[i] - i] += 1
        
        return ans
        
        
        
        