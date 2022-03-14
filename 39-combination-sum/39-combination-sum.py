class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ans = []
        candidates.sort()
        
        def helper(i,s):
            if i == len(candidates) or sum(s) >= target:
                if sum(s) == target:
                    ans.append(s[::])
                return
            
            s.append(candidates[i])
            helper(i,s)
            s.pop()
            
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            
            helper(i+1,s)
            
        helper(0,[])
        return ans
        