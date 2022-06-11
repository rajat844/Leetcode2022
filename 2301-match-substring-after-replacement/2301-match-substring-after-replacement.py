from collections import defaultdict
class Solution:
    def matchReplacement(self, s: str, sub: str, mappings: List[List[str]]) -> bool:
        n = len(s)
        k = len(sub)
        
        st = defaultdict(set)
        
        for i in range(len(mappings)):
            st[mappings[i][0]].add(mappings[i][1])
        
        
        for i in range(n-k+1):
            flag = True
            for j in range(k):
                x = s[i+j]
                y = sub[j]
                if x == y or x in st[y]:
                    continue
                else:
                    flag = False
                    break
            if flag == True:
                return True
        
        return False
                
            