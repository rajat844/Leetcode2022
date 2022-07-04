from collections import deque
import math
class Solution:
    def findMaxValueOfEquation(self, p: List[List[int]], k: int) -> int:
        ans = -math.inf
        st = deque()
        for i in range(len(p)):
            while len(st) > 0 and p[i][0] - p[st[0]][0] > k:
                st.popleft()
            
            if len(st) > 0:
                x = p[i][0] + p[i][1] - p[st[0]][0] + p[st[0]][1]
                ans = max(ans,x)
                
            while len(st) > 0 and p[st[-1]][0]-p[st[-1]][1] > p[i][0] - p[i][1]:
                st.pop()
            
            st.append(i)
        
        return ans
        