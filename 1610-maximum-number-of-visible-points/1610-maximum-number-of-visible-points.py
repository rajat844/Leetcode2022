class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        def getAngle(p):
            angle = math.atan2(p[0]-location[0],p[1]-location[1])/(2*math.pi) * 360
            if angle < 0:
                angle += 360
            
            return angle
        
        angles = []
        same = 0
        
        for i in range(len(points)):
            if points[i] == location:
                same += 1
            else:
                angles.append(getAngle(points[i]))

        angles.sort()
        st = deque()
        ans = 0
        
        for i in range(len(angles)):
            st.append(angles[i])
            while angles[i] - st[0] > angle:
                st.popleft()
            ans = max(ans,len(st))
        
        for i in range(len(angles)):
            angles[i] += 360
            st.append(angles[i])
            while angles[i] - st[0] > angle:
                st.popleft()
            ans = max(ans,len(st))
        
        return ans+same