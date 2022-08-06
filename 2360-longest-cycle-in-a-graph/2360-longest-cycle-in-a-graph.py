class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        def dfs(node,st):
            nonlocal ans
            if node == -1:
                return 
            if node in visited:
                cnt = -1
                for i in range(len(st)):
                    if node == st[i]:
                        cnt = i
                if cnt == -1:
                    return 
                ans = max(ans,len(st)-cnt)
                return 
            st.append(node)
            visited.add(node)
            dfs(edges[node],st)
                
        ans = -1
        visited = set()
        for i in range(len(edges)):
            if i in visited:
                continue
            dfs(i,[])
        
        return ans