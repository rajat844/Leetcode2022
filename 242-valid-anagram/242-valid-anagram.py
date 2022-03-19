from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        st = defaultdict(int)
        for x in s:
            st[x] += 1
        for x in t:   
            st[x] -= 1
        
        for x in st:
            if st[x] != 0:
                return False
        return True
        