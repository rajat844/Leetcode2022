from collections import deque
import math
class Solution:
    def findMaxValueOfEquation(self, p: List[List[int]], k: int) -> int:
        st = deque()
        ans = -math.inf
        n = len(p)
        for i in range(n):
            while len(st) > 0 and  p[i][0] - p[st[0]][0] > k:
                st.popleft()
            
            if len(st) > 0 :
                ans = max(ans,p[st[0]][1] - p[st[0]][0] + p[i][1] + p[i][0])
            
            while len(st) > 0 and p[st[-1]][1] - p[st[-1]][0] < p[i][1] - p[i][0]:
                st.pop()
            
            st.append(i)
        
        return ans
        