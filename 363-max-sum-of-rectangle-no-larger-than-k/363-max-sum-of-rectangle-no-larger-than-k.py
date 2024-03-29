
from sortedcontainers import SortedList
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        ans = -math.inf
        for r1 in range(m):
            arr = [0] * n  # arr[i] is sum(matrix[r1][c]...matrix[r2][c])
            for r2 in range(r1, m):
                for c in range(n): arr[c] += matrix[r2][c]
                ans = max(ans, self.maxSumSubAarray(arr, n, k))
        return ans

    def maxSumSubAarray(self, arr, n, k):
        right = 0  # PrefixSum so far
        seen = SortedList([0])
        ans = -math.inf
        for i in range(n):
            right += arr[i]
            left = self.ceiling(seen, right - k)  # right - left <= k -> left >= right - k
            if left != None:
                ans = max(ans, right - left)
            seen.add(right)
        return ans

    def ceiling(self, sortedList, key):  # O(logN)
        idx = sortedList.bisect_left(key)
        if idx < len(sortedList): return sortedList[idx]
        return None
        