class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()

        a = list(s)
        a = a[::-1]
        s = ' '.join(a)
        return s
        