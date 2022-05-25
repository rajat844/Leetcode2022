from collections import deque
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        ans = sum(cardPoints[:k])
        maxans = ans
        
        for i in range(1,k+1):
            ans = ans + cardPoints[-i] - cardPoints[k-i]
            maxans = max(ans,maxans)
        
        return maxans
            
            