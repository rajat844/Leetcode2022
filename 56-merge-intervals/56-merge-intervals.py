class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals,key = lambda x:x[0])
        curr = intervals[0]
        n = len(intervals)
        ans = []
        for i in range(n):
            if curr[0] <= intervals[i][0] <= curr[1]:
                curr[1] = max(curr[1],intervals[i][1])
            else:
                ans.append(curr)
                curr = intervals[i]
                
        ans.append(curr)
        return ans
        