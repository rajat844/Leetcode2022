from collections import defaultdict
class Solution:
    def countExcellentPairs(self, nums: List[int], k: int) -> int:
        st = defaultdict(int)
        s = set(nums)
        
        for x in s:
            cnt = bin(x).count("1")
            st[cnt] += 1
            
        ans = 0
        for i in range(1,30):
            for j in range(1,30):
                if i + j >= k:
                    ans += st.get(i,0) * st.get(j,0)
        
        return ans