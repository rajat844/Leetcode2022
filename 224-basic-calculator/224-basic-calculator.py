class Solution:
    def calculate(self, s: str) -> int:
        st = []
        sign = 1
        ans = 0
        currNo = 0
        
        i = 0
        
        while i < len(s):
            if s[i].isdigit():
                currNo = int(s[i])
                while i+1 < len(s) and s[i+1].isdigit():
                    i += 1
                    currNo = currNo * 10 + int(s[i])
                ans += sign * currNo
                currNo = 0
                sign = 1
            elif s[i] == "+":
                sign = 1
            elif s[i] == "-":
                sign = -1
            elif s[i] == "(":
                st.append(ans)
                st.append(sign)
                sign = 1
                ans = 0
            elif s[i] == ")":
                ans = ans * st.pop()
                ans += st.pop()
            
            i += 1
        
        return ans
            
            
        