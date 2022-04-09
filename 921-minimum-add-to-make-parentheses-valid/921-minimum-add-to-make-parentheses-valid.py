class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        if len(s) == 0:
            return 0
        st = []
        ans = 0
        
        for c in s:
            if c == '(':
                st.append(c)
            elif len(st) > 0 and c == ')':
                st.pop()
            else:
                ans += 1
        
        ans += len(st)
        return ans
        
        