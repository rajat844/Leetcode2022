class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        
        i = 0 
        j = 0
        cnt = []
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                cnt.append(nums1[i])
                i += 1
                j += 1
            
            elif nums1[i] > nums2[j]:
                j += 1
            else :
                i += 1
            
            while 0 < i < len(nums1) and nums1[i] == nums1[i-1]:
                i += 1
        
        return cnt