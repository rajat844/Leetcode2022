class Solution:
    def simplifyPath(self, path: str) -> str:
        st = []
        curr = ""
        for ch in path + "/":
            if ch == "/":
                if curr == "..":
                    if len(st) > 0 :
                        st.pop()
                elif curr != "" and curr != ".":
                    st.append(curr)
                curr = ""
            else:
                curr += ch
        
        return "/" + "/".join(st)