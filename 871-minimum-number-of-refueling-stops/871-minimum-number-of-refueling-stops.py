class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        pq = []
        ans = 0
        psn = 0
        while startFuel < target:
            while psn < len(stations) and stations[psn][0] <= startFuel:
                heapq.heappush(pq,-stations[psn][1])
                psn += 1
            
            if len(pq) == 0 :
                return -1
            startFuel += -heapq.heappop(pq)
            ans += 1
        
        return ans
                
        
        
                
            
            
            
        