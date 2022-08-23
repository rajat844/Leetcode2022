class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        st = []
        rem = len(nums) - k
        ans = math.inf
        for i in range(len(nums)):
            while len(st) > 0 and rem > 0 and st[-1] > nums[i]:
                st.pop()
                rem -= 1
            
            st.append(nums[i])
            
        return st[:k]
        
        
        