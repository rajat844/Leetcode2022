class Solution:
    def countArrangement(self, n: int) -> int:
        def helper(i):
            if i == n:
                nonlocal ans
                ans += 1
                return
            
            for x in range(i,n):
                arr[i],arr[x] = arr[x],arr[i]
                if arr[i] % (i+1)== 0 or (i+1) % arr[i] == 0:
                    helper(i+1)
                arr[i],arr[x] = arr[x],arr[i]
         
        ans = 0
        arr = [i for i in range(1,n+1)]
        helper(0)
        return ans
    