class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        ans = 0
        curr = -math.inf
        for i in range(len(intervals)):
            if intervals[i][0] < curr:
                ans += 1
                curr = min(curr,intervals[i][1])
            else :
                curr = intervals[i][1]
        
        return ans