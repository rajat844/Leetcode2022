class Solution:
    def strStr(self, heystack: str, needle: str) -> int:
        if needle == '':
            return 0
        
        for i in range(len(heystack) - len(needle) +1):
            if heystack[i: i+len(needle)] == needle:
                return i
        return -1
        