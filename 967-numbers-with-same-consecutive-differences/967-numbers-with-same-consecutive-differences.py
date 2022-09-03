class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        if n == 1:
            return [i for i in range(10)]
        
        def dfs(i,n):
            if n == 0:
                ans.append(i)
                return 
            
            tail = i%10
            
            if tail + k < 10:
                dfs(i*10 + tail+k,n-1)
                
            if k > 0 and tail - k >= 0:
                dfs(i*10 + tail-k,n-1)
        
        ans = []
        
        for i in range(1,10):
            dfs(i,n-1)
            
        return ans
        