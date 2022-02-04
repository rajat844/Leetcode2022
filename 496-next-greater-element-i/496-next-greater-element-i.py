class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        mapping = {}
        
        for i in reversed(nums2):
            while len(stack) > 0 and i >= stack[-1]:
                stack.pop()
                
            if len(stack) == 0:
                mapping[i] = -1
            else :
                mapping[i] = stack[-1]
            stack.append(i)
        ans = []
        
        for i in range(len(nums1)):
            ans.append(mapping[nums1[i]])
        
        return ans
            
                
                
            
        