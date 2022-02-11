import math
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2) :
            return self.findMedianSortedArrays(nums2,nums1)
        
        n = len(nums1)
        m = len(nums2)
        md = (n+m+1)>>1
        l = 0
        h = n
        
        while l <= h:
            cut1 = (h+l)>>1
            cut2 = md - cut1
            
            l1 = -math.inf if cut1 == 0 else nums1[cut1-1]
            l2 = -math.inf if cut2 == 0 else nums2[cut2-1]
            r1 = math.inf if cut1 == n else nums1[cut1]
            r2 = math.inf if cut2 == m else nums2[cut2]
            
            if l1 <= r2 and l2 <= r1:
                if (m+n)%2 == 0:
                    return (max(l1,l2)+min(r1,r2))/2
                else :
                    return max(l1,l2)
            elif l1 > r2 :
                h = cut1-1
            else :
                l = cut1+1
                
        return 0.0
        
        
        