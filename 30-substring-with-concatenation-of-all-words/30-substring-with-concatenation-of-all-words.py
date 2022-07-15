from collections import defaultdict
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        fr = defaultdict(int)
        
        total = len(words)
        wlen = len(words[0])
        
        for i in range(total):
            fr[words[i]] += 1
        
        n = len(s) - total*wlen + 1
        ans = []
        
        for i in range(n):
            st = defaultdict(int)
            for j in range(total):
                wInd = i + j * wlen
                w = s[wInd:wInd+wlen]
                if w not in fr:
                    break
                
                st[w] += 1
                if st[w] > fr[w]:
                    break
                if j+1 == total:
                    ans.append(i)
        
        return ans
        
        
        