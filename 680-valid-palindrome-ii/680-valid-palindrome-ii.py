class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l <= r:
            if s[l] != s[r]:
                string1 = s[l+1:r+1]
                string2 = s[l:r]
                if string1 == string1[::-1] or string2 == string2[::-1]:
                    return True
                else:
                    return False
            else :
                l += 1
                r -= 1
            
        return True