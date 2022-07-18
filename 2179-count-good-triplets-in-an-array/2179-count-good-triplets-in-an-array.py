from sortedcontainers import SortedList
class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        pos = [0 for i in range(len(nums2))]
        
        for i in range(len(nums2)):
            pos[nums2[i]] = i
        
        pos2,pre = SortedList([pos[nums1[0]]]),[0]
        for i in range(1,len(nums1)):
            pos2.add(pos[nums1[i]])
            pre.append(pos2.bisect_left(pos[nums1[i]]))
            
        pos2,suf = SortedList([pos[nums1[-1]]]),[0]
        for i in range(len(nums1)-2,-1,-1):
            idx = pos2.bisect(pos[nums1[i]])
            suf.append(len(pos2) - idx)
            pos2.add(pos[nums1[i]])
        suf.reverse()
        
        ans = 0
        for i in range(len(suf)):
            ans += suf[i] * pre[i]
        return ans