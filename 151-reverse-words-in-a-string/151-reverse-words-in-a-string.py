class Solution:
    def reverseWords(self, s: str) -> str:
        st = list(map(str,s.strip().split()))
        st = st[::-1]
        s = " ".join(st)
        
        return s
        
        