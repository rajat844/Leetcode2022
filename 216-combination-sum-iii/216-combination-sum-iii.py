class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        arr = [1,2,3,4,5,6,7,8,9]
        def helper(idx,x,s):
            if idx == len(arr) or x == k:
                if sum(s) == n and x == k:
                    ans.append(s[::])    
                return 
            
            for i in range(idx,9):
                s.append(arr[i])
                helper(i+1,x+1,s)
                s.pop()
               
        ans = []
        helper(0,0,[])
        
        return ans
                
            
        