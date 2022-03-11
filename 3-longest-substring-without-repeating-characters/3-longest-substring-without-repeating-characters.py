class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        start = 0
        ans = 0
        for i in range(len(s)):
            if s[i] in mp and start <= mp[s[i]]:
                start = mp[s[i]] + 1
            else :
                ans = max(ans,i-start + 1)
            mp[s[i]] = i
        return ans
                
            
        