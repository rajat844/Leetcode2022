class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        def dfs(node,st,l):
            nonlocal ans
            if node == -1:
                return 
            if node in visited:
                cnt = -1
                if node in st:
                    cnt = st[node]
                if cnt == -1:
                    return 
                ans = max(ans,l-cnt)
                return 
            st[node] = l
            visited.add(node)
            dfs(edges[node],st,l+1)
                
        ans = -1
        visited = set()
        for i in range(len(edges)):
            if i in visited:
                continue
            dfs(i,{},0)
        
        return ans