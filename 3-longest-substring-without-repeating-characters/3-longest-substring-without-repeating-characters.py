class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp  = {}
        strt = 0
        ans = 0
        
        for i in range(len(s)):
            if s[i] in mp and strt <= mp[s[i]]:
                strt = mp[s[i]] + 1
            else:
                ans = max(ans,i-strt + 1)
            mp[s[i]] = i
        
        return ans
             
        