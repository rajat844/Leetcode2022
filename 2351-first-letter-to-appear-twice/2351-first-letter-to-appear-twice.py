from collections import defaultdict
class Solution:
    def repeatedCharacter(self, s: str) -> str:
        st = defaultdict(int)
        for i in range(len(s)):
            st[s[i]] += 1
            if st[s[i]] > 1:
                return s[i]