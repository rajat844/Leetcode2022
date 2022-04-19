class Solution:
    def firstUniqChar(self, s: str) -> int:
        st = [0 for i in range(26)]
        
        for i in range(len(s)):
            st[ord(s[i]) - ord('a')] += 1
        
        for i in range(len(s)):
            if st[ord(s[i]) - ord('a')] == 1:
                return i
        
        return -1
        