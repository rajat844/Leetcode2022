class Solution:
    def leastInterval(self,tasks, n) -> int:
        dic = defaultdict(int)
        for i in range(len(tasks)):
            dic[tasks[i]] += 1
        st = []
        for x in dic:
            st.append(-dic[x])
        
        heapq.heapify(st)
        time = 0
        q = deque()
        
        while len(st) > 0 or len(q) > 0:
            time += 1
            if len(st) > 0:
                x = 1+ heapq.heappop(st)
                if x != 0:
                    q.append([x,time+n])
                              
            while len(q) > 0 and q[0][1] == time:
                heapq.heappush(st,q.popleft()[0])
        
        return time
                              
                
        
            