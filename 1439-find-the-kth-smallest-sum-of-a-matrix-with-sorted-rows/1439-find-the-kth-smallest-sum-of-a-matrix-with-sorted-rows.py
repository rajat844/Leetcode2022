import heapq
class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        n = len(mat)
        m = len(mat[0])
        
        s = sum(mat[i][0] for i in range(n))
        choice = [s] + [0]*n
        seen = set()
        seen.add(tuple(choice))
        pq = [choice]
        
        while k-1 :
            k -= 1
            prev = heappop(pq)
           
            for  i in range(n):
                if prev[i+1] == m-1:
                    continue
                nex = prev[::]
                nex[0] -= mat[i][nex[i+1]]
                nex[i+1] += 1
                nex[0] += mat[i][nex[i+1]]
                
                if tuple(nex) not in seen:
                    seen.add(tuple(nex))
                    heapq.heappush(pq,nex)
        
        return pq[0][0]
                    
        