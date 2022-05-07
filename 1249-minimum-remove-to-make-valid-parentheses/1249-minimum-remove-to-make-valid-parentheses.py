class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        st = []
        ans = []
        
        for i in range(len(s)):
            if s[i] == "(":
                st.append(i)
                ans.append("(")
            elif s[i] == ")":
                if len(st) > 0:
                    st.pop()
                    ans.append(")")
                else:
                    ans.append("")
            else:
                ans.append(s[i])
        print(ans)
        while len(st) > 0:
            i = st.pop()
            ans[i] = ""
        
        return ''.join(ans)
                
                