class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def helper(node):
            visited[node] = True
            loopvisited[node] = True
            
            for x in adj[node]:
                if visited[x] == False:
                    if helper(x) == True:
                        return True
                elif loopvisited[x] == True:
                    return True
            
            loopvisited[node] = False
            return False
            
            
        adj = {}
        for i in range(numCourses):
            adj[i] = []
        
        for i in range(len(prerequisites)):
            adj[prerequisites[i][1]].append(prerequisites[i][0])
            
        visited = [False for i in range(numCourses)]
        loopvisited = [False for i in range(numCourses)]
        
        for i in range(numCourses):
            if visited[i] == False:
                if helper(i) is True:
                    return False
                
        return True