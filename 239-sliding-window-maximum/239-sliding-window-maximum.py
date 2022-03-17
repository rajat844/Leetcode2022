from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        ans = []
        st = deque()
        
        for i in range(len(nums)):
            if len(st) > 0 and st[0] < i-k + 1:
                st.popleft()
            while len(st) > 0 and nums[st[-1]] < nums[i]:
                st.pop()
            
            st.append(i)
            if i >= k - 1:
                ans.append(nums[st[0]])
            
        return ans