class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        nexsmaller = []
        st = []
        for i in range(n-1,-1,-1):
            while len(st) > 0 and heights[i] <= heights[st[-1]]:
                st.pop()
            
            if len(st) == 0:
                nexsmaller.append(n-1)
            else:
                nexsmaller.append(st[-1] - 1)
            
            st.append(i)
            
        nexsmaller = nexsmaller[::-1]   
        prevsmaller = []
        st = []
        
        for i in range(n):
            while len(st) > 0 and heights[i] <= heights[st[-1]]:
                st.pop()
            
            if len(st) == 0:
                prevsmaller.append(0)
            
            else:
                prevsmaller.append(st[-1] + 1 )
            
            st.append(i)
            
        ans = 0
        for i in range(n):
            temp = heights[i] *(nexsmaller[i] - prevsmaller[i] + 1)
            ans = max(temp,ans)
        
        return ans
            
            