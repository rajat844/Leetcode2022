class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        if k == len(cookies):
            return max(cookies)
        arr = [0 for i in range(k)]
        ans = math.inf
        
        def recursion(i):
            nonlocal ans
            if i == len(cookies):
                curr = max(arr)
                ans = min(ans,curr)
                return 
            
            for j in range(k):
                arr[j] += cookies[i]
                recursion(i+1)
                arr[j] -= cookies[i]
                if arr[j] == 0 :
                    break
        
        recursion(0)
        return ans
                
                
        