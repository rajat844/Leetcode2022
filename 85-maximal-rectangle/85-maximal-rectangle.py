class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def maxArea(arr):
            st = []
            area = 0
            
            for i in range(len(arr) + 1):
                while len(st) > 0 and (i == len(arr) or arr[i] <= arr[st[-1]]):
                    h = arr[st.pop()]
                    w = 0
                    if len(st) == 0:
                        w = i
                    else:
                        w = i - st[-1] - 1
                    area = max(area,h*w)
                st.append(i)
            
            return area
        
        temp = [0 for i in range(len(matrix[0]))]
        ans = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "0":
                    temp[j] = 0
                else:
                    temp[j] += 1
            
            ans = max(ans,maxArea(temp))
            
        return ans
            
            
                    
                    
        