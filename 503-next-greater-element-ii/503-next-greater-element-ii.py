class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        st = []
        n = len(nums)
        ans = [0 for i in range(n)]
        
        for i in range(2*n - 1,-1,-1):
            while len(st) > 0 and nums[st[-1]] <= nums[i%n]:
                st.pop()
            
            if len(st) == 0:
                ans[i%n] = -1
            
            else:
                ans[i%n] = nums[st[-1]]
                
            st.append(i%n)
        
        return ans
                
        