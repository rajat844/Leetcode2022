class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        st = {}
        start = 0
        ans = 0
        
        for i in range(n):
            if s[i] in st and start <= st[s[i]]:
                start = st[s[i]] + 1
            
            else:
                ans = max(ans,i-start+1)
            
            st[s[i]] = i
        
        return ans
             
            
            
            
             
        