class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        st = []
        
        n = len(nums)
        answer = [-1] * n
        for i in range(2*n-1,0,-1):
            while len(st) > 0 and nums[i%n] >= st[-1]:
                st.pop()
            
            if len(st) == 0:
                answer[i%n] = -1
            else :
                answer[i%n] = st[-1]
            st.append(nums[i%n])
        return answer
                
                
        