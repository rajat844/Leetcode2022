from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        storage = deque()
        ans = []
        for i in range(len(nums)):
            if len(storage) > 0 and storage[0] == i-k:
                storage.popleft()
            while len(storage) > 0 and nums[storage[-1]] <= nums[i]:
                storage.pop()
            storage.append(i)
            if i >= k-1 :
                ans.append(nums[storage[0]])
        return ans
            