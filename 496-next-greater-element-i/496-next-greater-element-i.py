class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        st = []
        dic = {}
        
        for i in range(len(nums2)-1,-1,-1):
            while len(st) > 0 and nums2[i] > st[-1]:
                st.pop()
            
            if len(st) == 0:
                dic[nums2[i]] = -1
            else :
                dic[nums2[i]] = st[-1]
            
            st.append(nums2[i])
        
        ans = []
        for i in range(len(nums1)):
            ans.append(dic[nums1[i]])
        
        return ans
            
            
        