class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        dic = Counter(tasks)
        st = []
        for x in dic:
            heapq.heappush(st,-dic[x])
        
        q = deque()
        time = 0
        
        while len(st) > 0 or len(q) > 0:
            time += 1
            if len(st) > 0:
                x = 1 + heapq.heappop(st)
                if x != 0:
                    q.append([x,time+n])
            
            if len(q) > 0 and q[0][1] == time:
                heapq.heappush(st,q.popleft()[0])
                
        return time
                
            
             
        