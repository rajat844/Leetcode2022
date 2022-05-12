class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums)):
            nums[i] = str(nums[i])
            
        def srt(n1,n2):
            if n1 + n2 > n2+n1:
                return -1
            else:
                return 1
        
        nums.sort(key = cmp_to_key(srt))
        
        return str(int(''.join(nums)))
        