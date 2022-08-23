class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        rem = len(nums) - k
        st = []
        
        for x in nums:
            while len(st) > 0 and rem > 0 and st[-1] > x:
                st.pop()
                rem -= 1
            st.append(x)
        
        return st[:k]
        
        