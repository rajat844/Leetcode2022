class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        
        jobs = []
        for i in range(len(startTime)):
            jobs.append((startTime[i],endTime[i],profit[i]))
        
        jobs.sort(key = lambda x :x[1])
        
        n = len(jobs)
        m = jobs[-1][1] 
        
        dp = [-1 for i in range(n)]
        
        dp[0] = jobs[0][2]
        
        for i in range(n):
            inc = jobs[i][2]
            last = -1
            low = 0
            high = i-1
            
            while low <= high :
                mid = (low + high)//2
                if jobs[mid][1] <= jobs[i][0]:
                    last = mid
                    low = mid+1
                else :
                    high = mid-1
            if last != -1:
                inc += dp[last]
            exc = dp[i-1]
            dp[i] = max(inc,exc)
        
        return dp[n-1]