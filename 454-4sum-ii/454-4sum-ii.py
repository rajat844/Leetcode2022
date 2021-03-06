from collections import defaultdict
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        st = defaultdict(int)
        n = len(nums1)
        
        for i in range(n):
            for j in range(n):
                st[nums1[i]+nums2[j]] += 1
        
        ans = 0
        for i in range(n):
            for j in range(n):
                x = nums3[i]+nums4[j]
                if 0-x in st:
                    ans += st[0-x]
                
        return ans