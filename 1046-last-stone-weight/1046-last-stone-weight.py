class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-1*n for n in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            a = heapq.heappop(stones)
            b = heapq.heappop(stones)
            
            if a - b < 0:
                heapq.heappush(stones,a-b)
        
        if len(stones) == 0:
            return 0
        else:
            return -stones[0]
            
        