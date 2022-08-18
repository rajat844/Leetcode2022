class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def helper(i,s):
            if i == n+1 or len(s) == k:
                if len(s) == k:
                    ans.append(s[::])
                return 
            helper(i+1,s+[i])
            helper(i+1,s)
        
        ans = []
        helper(1,[])
        return ans
        