class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        st1 = Counter(ransomNote)
        st2 = Counter(magazine)
        
        if len(st2) < len(st1):
            return False
        
        for x in st1:
            if x not in st2 or st2[x] < st1[x]:
                return False
        
        return True
        