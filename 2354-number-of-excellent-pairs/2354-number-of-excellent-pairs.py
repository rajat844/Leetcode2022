from collections import defaultdict
class Solution:
    def countExcellentPairs(self, nums: List[int], k: int) -> int:
        st = defaultdict(int)
        ans = 0
        s = set(nums)
        
        for x in s:
            c = bin(x).count("1")
            st[c] += 1
        
        for i in range(1,30):
            for j in range(1,30):
                if i + j >= k:
                    ans += st.get(i,0) * st.get(j,0)
        return ans
        