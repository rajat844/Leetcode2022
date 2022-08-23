class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        s = list(str(n))
        i = 1
        
        while i < len(s) and s[i] >= s[i-1]:
            i += 1
        
        while i > 0 and i < len(s) and s[i] < s[i-1]:
            s[i-1] = str(int(s[i-1]) - 1)
            i -= 1
        
        for j in range(i+1,len(s)):
            s[j] = "9"
        
        return int("".join(s))
        