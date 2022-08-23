class Solution:
    def smallestSubsequence(self, s: str) -> str:
        st = Counter(s)
        stack = []
        used = set()
        
        for i in range(len(s)):
            st[s[i]] -= 1
            if s[i] in used:
                continue
            while len(stack) > 0 and ord(stack[-1]) > ord(s[i]) and st[stack[-1]] > 0:
                used.remove(stack[-1])
                stack.pop()
                
            stack.append(s[i])
            used.add(s[i])
        
        return "".join(stack)
                
            
        
        
        