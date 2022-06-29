import math
from collections import deque
class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        n = len(points)
        ans = -math.inf
        
        st = deque()
        
        for i in range(n):
            while len(st) > 0 and points[i][0] - points[st[0]][0] > k:
                st.popleft()
            
            if len(st) > 0:
                ans = max(ans,points[st[0]][1] - points[st[0]][0] + points[i][1] + points[i][0])
                
            while len(st) > 0 and points[st[-1]][1] - points[st[-1]][0] < points[i][1] - points[i][0]:
                st.pop()
            
            st.append(i)
        
        return ans
                                         
                                         
                