class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        st = []
        dic = {}
        n = len(nums2)
        for i in range(n-1,-1,-1):
            while len(st) > 0 and nums2[i] >= nums2[st[-1]]:
                st.pop()
            if len(st) > 0:
                dic[nums2[i]] = nums2[st[-1]]
            else :
                dic[nums2[i]] = -1
            st.append(i)
        ans = []   
        for i in range(len(nums1)):
            ans.append(dic[nums1[i]])
            
        return ans
            
            
        