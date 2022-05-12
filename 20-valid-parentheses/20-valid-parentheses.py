class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        
        for i in range(len(s)):
            if s[i] in set(['(','{','[']):
                st.append(s[i])
            elif s[i] == "}":
                if len(st) > 0 and st[-1] == "{":
                    st.pop()
                else:
                    return False
            elif s[i] == ")":
                if len(st) > 0 and st[-1] == "(":
                    st.pop()
                else:
                    return False
            elif s[i] == "]":
                if len(st) > 0 and st[-1] == "[":
                    st.pop()
                else:
                    return False
        
        if len(st) != 0:
            return False
        return True
        