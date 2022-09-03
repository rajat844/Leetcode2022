class Solution:
    def maximumRows(self, mat: List[List[int]], cols: int) -> int:
        def helper(i,cols):
            nonlocal ans
            if i == m or cols == 0:
                cnt = 0
                for x in range(n):
                    check = True
                    for y in range(m):
                        if mat[x][y] == 1 and visited[y] == False:
                            check = False
                            
                    if check == True:
                        cnt += 1
                
                ans = max(cnt,ans)
                return 
            
            visited[i] = True
            helper(i+1,cols-1)
            visited[i] = False
            helper(i+1,cols)
                            
                        
                        
        n = len(mat)
        m = len(mat[0])
        visited = [False for i in range(m)]
        ans = 0
        helper(0,cols)
        return ans
        