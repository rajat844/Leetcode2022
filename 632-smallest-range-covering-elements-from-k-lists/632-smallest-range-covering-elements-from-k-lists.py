class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        ans = [1e-5, 1e5]
        
        mx = 0
        st = []
        
        for i in range(len(nums)):
            st.append((nums[i][0],i,0))
            mx = max(mx,nums[i][0])
        
        heapq.heapify(st)
        
        while len(st) == len(nums):
            mn , row, col = heapq.heappop(st)
            
            if mx - mn < ans[1] - ans[0]:
                ans = [mn,mx]
            
            if col+1 < len(nums[row]):
                heapq.heappush(st,(nums[row][col+1],row,col+1))
                mx = max(mx,nums[row][col+1])
        
        return ans
            