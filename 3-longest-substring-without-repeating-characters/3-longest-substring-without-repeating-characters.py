class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        st = {}
        start = 0
        
        for i in range(len(s)):
            if s[i] in st and st[s[i]] >= start:
                start = st[s[i]] + 1
            ans = max(ans,i - start + 1)
            st[s[i]] = i
        
        return ans
        