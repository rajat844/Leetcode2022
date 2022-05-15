class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        lb = bottom
        ans = 0
        special.sort()
        
        
        for i in range(len(special)):
            cns = special[i] - lb
            ans = max(cns,ans)
            lb = special[i] + 1
            
        ans = max(ans,top - lb + 1)
        
        return ans
        
        
        