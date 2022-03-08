class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        n = len(nums)

        def helper(s, i):
            if i == n:
                if s not in ans:
                    t = []
                    for x in range(len(s)):
                        t.append(s[x])
                    ans.append(t)
                return

            for index in range(i, n):
                if index > i and nums[index] == nums[index-1]:
                    continue
                s.append(nums[index])
                helper(s,index+1)
                s.pop()            
                helper(s,index+1)
        s = []
        helper(s, 0)
        return ans
        