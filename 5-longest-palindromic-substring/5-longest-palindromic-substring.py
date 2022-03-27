class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        
        for i in range(len(s)):
            j = i
            k = i
            
            while j-1 >= 0 and s[j-1] == s[i]:
                j -= 1
            
            while k+1 < len(s) and s[k+1] == s[i]:
                k += 1
            
            while j-1 >= 0 and k+1 < len(s) and s[j-1] == s[k+1]:
                j -= 1
                k += 1
            
            temp = s[j:k+1]
            if len(temp) > len(ans):
                ans = temp
        
        return ans
            
            