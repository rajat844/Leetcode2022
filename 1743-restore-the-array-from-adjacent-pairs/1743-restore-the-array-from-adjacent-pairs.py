from collections import defaultdict
class Solution:
    def restoreArray(self, a: List[List[int]]) -> List[int]:
        def dfs(node):
            nonlocal ans
            ans.append(node)
            
            for x in st[node]:
                if x not in seen :
                    seen.add(x)
                    dfs(x)                  
            
            
            
        st = defaultdict(list)
        for i in range(len(a)):
            st[a[i][0]].append(a[i][1])
            st[a[i][1]].append(a[i][0])
            
        start = None
        
        for key,value in st.items():
            if len(value) == 1:
                start = key
                break
        
        ans = []
        seen = set()
        seen.add(start)
        dfs(start)
        return ans
            
        