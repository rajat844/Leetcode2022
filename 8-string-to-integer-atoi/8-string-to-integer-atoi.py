class Solution:
    def myAtoi(self, s: str) -> int:
        ans = 0
        negative = 1
        i = 0
        
        while i < len(s) and s[i] == " ":
            i += 1
        
        if i < len(s) and s[i] == '-':
            i += 1
            negative = -1
            
        elif i < len(s) and s[i] == '+':
            i += 1 
            
            
        checker = set('0123456789')
        while i < len(s) and s[i] in checker:
            ans = ans * 10 + int(s[i])
            i += 1
        
        ans = negative*ans
        
        if ans < 0:
            return max(ans,-2**31)
        return min(ans,2**31 - 1 )