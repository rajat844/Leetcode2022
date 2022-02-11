class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        
        for i in range(len(s)):
            j = i
            k = i
            currstr = s[i]
            
            while(j+1 < len(s) and j >= 0 and s[i] == s[j+1]):
                j += 1
                currstr += s[j]
            while (k-1 >= 0 and k < len(s) and s[i] == s[k-1]):
                k -= 1
                currstr += s[k]
            
            while j+1 < len(s) and k-1 >= 0  and j > 0 and k < len(s) and s[j+1] == s[k-1]:
                j += 1
                k -= 1
                currstr = s[k] + currstr + s[j]
            
            if len(currstr) > len(ans):
                ans = currstr
        
        return ans
                    