from collections import defaultdict
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        st = defaultdict(list)
       
        nums.sort()
        nums1 = nums[::]
        for i in range(len(nums1)):
            total = 0
            while nums1[i]:
                total += nums1[i]%10
                nums1[i] //= 10
            st[total].append(i)
            
        ans = -1    
        for x in st:
            if len(st[x]) > 1:
                ans = max(nums[st[x][-1]] + nums[st[x][-2]],ans)
        return ans
                
                