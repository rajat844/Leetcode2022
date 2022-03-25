class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)

        for i in range(len(prerequisites)):
            adj[prerequisites[i][0]].append(prerequisites[i][1])
            
        visited = [False for i in range(numCourses)]
        dfsvisited = [False for i in range(numCourses)]

        def helper(node): 
            visited[node] = True
            dfsvisited[node] = True
            
            for x in adj[node]:
                if visited[x] == False:
                    if helper(x) == True:
                        return True
                elif dfsvisited[x] == True:
                    return True
            
            dfsvisited[node] = False
            ans.append(node)
            return False
        
        
        ans = []
        for i in range(numCourses):
            if visited[i] == False:
                if helper(i) == True:
                    return []
        
        return ans