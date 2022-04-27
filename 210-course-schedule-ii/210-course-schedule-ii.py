from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #adjacency list
        adj = {}
        for i in range(numCourses):
            adj[i] = []
            
        for i in range(len(prerequisites)):
            adj[prerequisites[i][1]].append(prerequisites[i][0])
        
        #count the courses need to done before any 
        count = [0 for i in range(numCourses)]
        
       
        for i in range(numCourses):
            for x in adj[i]:
                count[x] += 1
                
        st = deque()
        
         #pushed all courses with prerequisites is 0
        for i in range(numCourses):
            if count[i] == 0:
                st.append(i)
        
        ans = []
        while len(st) > 0:
            node = st.popleft()
            ans.append(node)
            
            for x in adj[node]:
                count[x] -= 1
                if count[x] == 0:
                    st.append(x)
        if len(ans) == numCourses:
            return ans
        return []
            