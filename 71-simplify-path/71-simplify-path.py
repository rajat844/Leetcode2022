class Solution:
    def simplifyPath(self, path: str) -> str:
        st = []
        curr = ""
        
        path += "/"
        for i in range(len(path)):
            if path[i] == "/":
                if curr == "..":
                    if len(st) > 0:
                        st.pop()
                elif curr != "" and curr != ".":
                    st.append(curr)
                curr = ""
            else:
                curr += path[i]
        
        return "/"+"/".join(st)