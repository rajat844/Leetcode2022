class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i = len(s) - 1
        back = 0
    
        
        res = ""
        
        while i >= 0:
            if s[i] == "#" or back != 0:
                if s[i] == "#":
                    back += 1
                else :
                    back -= 1
            else :
                res += s[i]
            i -= 1
        
        i = len(t) - 1
        back = 0
        res2 = ""
        
        while i >= 0:
            if t[i] == "#" or back != 0:
                if t[i] == '#':
                    back += 1
                else :
                    back -= 1
            else:
                res2 += t[i]
            i -= 1
    
        return res2 == res