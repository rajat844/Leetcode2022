class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        s = s.split()
        l = list(s)
        l.reverse()
        
        return ' '.join(l)
        