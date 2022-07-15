class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[None for i in range(n)]for j in range(n)]
        curr = 1
        l,r,t,b = 0,n-1,0,n-1
        
        while l <= r and t <= b:
            for i in range(l,r+1):
                ans[t][i] = curr
                curr += 1
            t += 1
            
            for i in range(t,b+1):
                ans[i][r] = curr
                curr += 1
            r -= 1
            
            if l <= r:
                for i in range(r,l-1,-1):
                    ans[b][i] = curr
                    curr += 1
                b -= 1
                
            if t <= b:
                for i in range(b,t-1,-1):
                    ans[i][l] = curr
                    curr += 1
                l += 1
        
        return ans
                
            