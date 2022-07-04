from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        st = defaultdict(int)
        
        for ch in t:
            st[ch] += 1
        
        l = 0
        ans = ""
        cnt1 = 0
        cnt = len(st)
        
        for r in range(len(s)):
            st[s[r]] -= 1
            if st[s[r]] == 0:
                cnt1 += 1
                
            while cnt1 == cnt and l <= r:
                if ans == "" or len(ans) > r-l+1:
                    ans = s[l:r+1]
                st[s[l]] += 1
                if st[s[l]] == 1:
                    cnt1 -= 1
                l += 1
        
        return ans