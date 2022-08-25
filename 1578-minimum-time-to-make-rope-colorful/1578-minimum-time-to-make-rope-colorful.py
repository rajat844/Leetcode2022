class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        currCh = None
        currCost = 0
        
        ans = 0
        
        for i in range(len(colors)):
            if currCh == colors[i]:
                if neededTime[i] > currCost:
                    ans += currCost
                    currCost = neededTime[i]
                else:
                    ans += neededTime[i]
            else:
                currCh = colors[i]
                currCost = neededTime[i]
        
        return ans
                
        