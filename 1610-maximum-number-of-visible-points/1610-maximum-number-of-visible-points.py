class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        def getAngle(p):
            a = math.atan2(p[0]-location[0],p[1]-location[1])/(2*math.pi) * 360
            if a < 0:
                a += 360
            
            return a
        
        same = 0
        arr = []
        for p in points:
            if p == location:
                same += 1
            else:
                arr.append(getAngle(p))
        
        arr.sort()
        st = deque()
        ans = 0
        
        for ele in arr:
            st.append(ele)
            while ele - st[0] > angle:
                st.popleft()
            ans = max(ans,len(st))
            
        for ele in arr:
            ele += 360
            st.append(ele)
            while ele - st[0] > angle:
                st.popleft()
            ans = max(ans,len(st))
            
        return ans+same
        
                
                