class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        
        ans = 0
        mul = 1
        
        for i in range(len(columnTitle) - 1,-1,-1):
            c = columnTitle[i]
            x = ord(c) - ord("A") + 1
            ans += mul * x
            mul *= 26
        
        return ans
            
            