class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        st = {}
        ans = []
        if numerator * denominator < 0:
            ans.append("-")
            numerator = abs(numerator)
            denominator = abs(denominator)
        
        q = numerator//denominator
        r = numerator%denominator
        ans.append(str(q))
        if r == 0:
            s = "".join(ans)
            return s
        else:
            ans.append(".")
        
        while r != 0:
            r = r*10
            q = r//denominator
            r = r%denominator
            ans += str(q)
            if r in st:
                ans.insert(st[r],"(")
                ans.append(")")
                break
            st[r] = len(ans)
            
        s = ''.join(ans)
        return s
        
        
        
        