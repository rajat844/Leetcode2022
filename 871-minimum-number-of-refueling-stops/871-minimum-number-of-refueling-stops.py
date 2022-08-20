class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        st = []
        ans = 0
        i = 0
        
        while startFuel < target:
            while i < len(stations) and startFuel >= stations[i][0]:
                heapq.heappush(st,-stations[i][1])
                i += 1
            if len(st) == 0:
                return -1
            startFuel += -heapq.heappop(st)
            ans += 1
        
        return ans
        