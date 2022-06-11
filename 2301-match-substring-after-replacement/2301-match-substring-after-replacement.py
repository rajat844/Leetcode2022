from collections import defaultdict
class Solution:
    def matchReplacement(self, s: str, sub: str, mappings: List[List[str]]) -> bool:
        n = len(s)
        m = len(sub)
        
        st = defaultdict(set)
        
        for i in range(len(mappings)):
            st[mappings[i][0]].add(mappings[i][1])
            
        
        for i in range(n-m+1):
            isTrue = True
            for j in range(m):
                x = s[i+j]
                y = sub[j]
                
                if x == y or x in st[y]:
                    continue
                else :
                    isTrue = False
                    break
                    
            if isTrue == True:
                return True
        
        return False
            