class Solution:
    def countPairs(self, nums: List[int]) -> int:
        ans = 0
        st = defaultdict(int)
        nums.sort()
        for i in range(len(nums)):
            for j in range(22):
                check = 1<<j
                x = check - nums[i]
                
                if x > nums[i]:
                    break
                if x in st:
                    ans += st[x]
                    
            st[nums[i]] += 1
        
        return ans % (10**9+7)