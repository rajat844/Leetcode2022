from collections import deque
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        st = list(s)
        for i in range(len(st)):
            if s[i] == "(":
                stack.append(i)
            if s[i] == ")":
                if len(stack) == 0:
                    st[i] = ''
                else:
                    stack.pop()
                    
        while len(stack) != 0:
            st[stack[-1]] = ""
            stack.pop()
        ans = ''.join(st)
        return ans
            