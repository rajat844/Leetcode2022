class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        def dfs(made,curr,start,limit):
            if made == k:
                return True
            if curr == limit:
                return dfs(made+1,0,0,limit)
            i = start
            while i < len(nums):
                if visited[i] or nums[i]+curr > limit:
                    i += 1
                    continue
                visited[i] = True
                if dfs(made,curr+nums[i],i+1,limit):
                    return True
                visited[i] = False
                
                while i+1 < len(nums) and nums[i+1] == nums[i]:
                    i += 1

                i += 1
                
            return False
        
        if len(nums) < k or sum(nums) % k:
            return False
        numSum = sum(nums)
        nums.sort(reverse = True)
        for x in nums:
            if x > numSum // k:
                return False
        visited = [False] * len(nums)
        return dfs(0,0,0,numSum//k)