class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        arr = []
        for i in range(len(nums)):
            arr.append((nums[i],i))
        arr.sort(reverse = True)
        arr = arr[:k]
        arr.sort(key = lambda x: x[1])
        
        ans = []
        for i in range(len(arr)):
            ans.append(arr[i][0])
        
        return ans