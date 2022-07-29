from collections import defaultdict
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        st = defaultdict(list)
        
        for i in range(len(pattern)):
            st[pattern[i]].append(i)
        
        ans = []
        for word in words:
            temp = defaultdict(list)
            for i in range(len(word)):
                temp[word[i]].append(i)
            
            if list(st.values()) == list(temp.values()):
                ans.append(word)
        
        return ans
            
        
        