class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        st = defaultdict(int)
        l = 0
        ans = 0
        
        for r in range(len(s)):
            st[s[r]] += 1
            while r-l+1 - max(st.values()) > k:
                st[s[l]] -= 1
                l += 1
            ans = max(ans,r-l+1)
        
        return ans
        