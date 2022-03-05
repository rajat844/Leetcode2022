from collections import defaultdict
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        def issubseq(word):
            curr = -1           
            for i in range(len(word)):
                char = word[i]
                if st[char]:
                    pos = bisect.bisect_right(st[char],curr)
                    if pos == len(st[char]):
                        return False
                    curr = st[char][pos]
                else:
                    return False
            return True
            
        
        st = defaultdict(list)
        
        for i in range(len(s)):
            st[s[i]].append(i)
            
        hashmap = {}
        
        count = 0
        for word in words:
            if word not in hashmap:
                if issubseq(word):
                    count += 1
                    hashmap[word] = True
                else:
                    hashmap[word] = False
            else :
                if hashmap[word]:
                    count += 1
                    
        return count
                