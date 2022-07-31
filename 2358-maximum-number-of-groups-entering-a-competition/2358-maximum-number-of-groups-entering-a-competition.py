class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        n = len(grades)
        ans = 0
        
        while n >= ans+1:
            ans += 1
            n -= ans
        
        return ans
        
        