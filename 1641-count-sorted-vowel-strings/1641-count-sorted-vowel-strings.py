class Solution:
    def countVowelStrings(self, n: int) -> int:
        ans = [1 for i in range(5)]
        
        for i in range(2,n+1):
            for i in range(3,-1,-1):
                ans[i] += ans[i+1]
        
        return sum(ans)