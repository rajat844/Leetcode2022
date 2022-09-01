class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def maxAreaHistogram(arr):
            st = []
            res = 0
            
            for i in range(len(arr)+1):
                while len(st) > 0 and (i == len(arr) or arr[i] <= arr[st[-1]]):
                    h = arr[st.pop()]
                    w = 0
                    if len(st) == 0:
                        w = i
                    else:
                        w = i - st[-1] - 1
                    
                    res = max(res,h*w)
                st.append(i)
            return res
        
        n = len(matrix)
        m = len(matrix[0])
        temp = [0 for i in range(m)]
        ans = 0
    
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == "0":
                    temp[j] = 0
                else:
                    temp[j] += 1
                    
            ans = max(ans,maxAreaHistogram(temp))
        
        return ans
            
        
        
                    
                                       
                    
        