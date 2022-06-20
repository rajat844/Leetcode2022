class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        st1 = {}
        st2 = {}
        for i in range(len(s)):
            if (s[i] in st1 and st1[s[i]] != t[i])or (t[i] in st2 and st2[t[i]] != s[i]) :
                return False
            else :
                st1[s[i]] = t[i]
                st2[t[i]] = s[i]

        return True
        