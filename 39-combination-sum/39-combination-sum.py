class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(candidates)
        
        def helper(index,s):
            if index == n or sum(s) >= target:
                if sum(s) == target:
                    temp = []
                    for e in s:
                        temp.append(e)
                    ans.append(temp)
                return
            s.append(candidates[index])
            helper(index,s)
            s.pop()
            helper(index+1,s)
        
        helper(0,[])
        return ans