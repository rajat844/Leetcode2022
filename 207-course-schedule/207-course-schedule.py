from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)

        for i in range(len(prerequisites)):
            adj[prerequisites[i][0]].append(prerequisites[i][1])

        visited = [False for i in range(numCourses)]
        dfsvisited = [False for i in range(numCourses)]

        def helper(node, parent):
            visited[node] = True
            dfsvisited[node] = True

            for x in adj[node]:
                if visited[x] == False:
                    if helper(x, node) == True:
                        return True
                elif dfsvisited[x] == True:
                    return True
            dfsvisited[node] = False
            return False

        for i in range(numCourses):
            if visited[i] == False:
                if helper(i, -1) == True:
                    return False

        return True