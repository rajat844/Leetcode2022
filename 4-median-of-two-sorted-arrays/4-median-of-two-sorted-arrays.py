import math
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2,nums1)
        
        n1 = len(nums1)
        n2 = len(nums2)
        
        l = 0
        h = n1
        
        while l<=h:
            mid1 = (l+h) >> 1
            mid2 = ((n1+n2+1)>>1) - mid1
            
            l1 = -math.inf if mid1 == 0 else nums1[mid1 - 1]
            l2 = -math.inf if mid2 == 0 else nums2[mid2 - 1]
            
            r1 = math.inf if mid1 == n1 else nums1[mid1]
            r2 = math.inf if mid2 == n2 else nums2[mid2]
            
            if l1 <= r2 and l2 <= r1:
                if (n1+n2) % 2 == 0:
                    l = max(l1,l2)
                    r = min(r1,r2)
                    return (l+r)/2
                else:
                    return max(l1,l2)
            
            elif l1 >= r2:
                h = mid1 - 1
            
            else :
                l = mid1 + 1
        
        return -1
        