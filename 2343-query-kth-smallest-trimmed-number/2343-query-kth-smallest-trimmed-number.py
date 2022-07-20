class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        ans = []
        for i,j in queries:
            temp = []
            for x in range(len(nums)):
                temp.append((int(nums[x][-j:]),x))
            temp.sort()
            ans.append(temp[i-1][1])
        return ans