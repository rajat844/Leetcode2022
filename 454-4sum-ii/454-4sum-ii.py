from collections import defaultdict
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:   
        st = defaultdict(int)
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                x = nums1[i]+nums2[j]
                st[x] += 1
        ans = 0
        for i in range(len(nums3)):
            for j in range(len(nums4)):
                x = nums3[i] + nums4[j]
                if -x in st:
                    ans += st[-x]
        
        return ans