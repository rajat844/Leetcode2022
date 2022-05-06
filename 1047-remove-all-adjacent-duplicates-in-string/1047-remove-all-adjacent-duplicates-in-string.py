class Solution:
    def removeDuplicates(self, s: str) -> str:
        st = []
        
        for char in s:
            if len(st) > 0 and char == st[-1]:
                st.pop()
            
            else:
                st.append(char)
        
        return ''.join(st)