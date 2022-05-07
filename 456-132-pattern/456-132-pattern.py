import math
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        s2 = -math.inf
        st = []
        
        for i in range(len(nums) - 1,-1,-1):
            if nums[i] < s2:
                return True
            else:
                while len(st) > 0 and nums[i] > st[-1]:
                    s2 = st[-1]
                    st.pop()
            
            st.append(nums[i])
        
        return False