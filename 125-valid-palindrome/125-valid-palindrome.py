class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = ""
        for i in range(len(s)):
            if ord("0") <= ord(s[i]) <= ord("9"):
                t += s[i]
            elif ord("A") <= ord(s[i]) <= ord("Z"):
                t += s[i].lower()
            elif ord("a") <= ord(s[i]) <= ord("z"):
                t += s[i]
    
        if t == t[::-1]:
            return True
        return False