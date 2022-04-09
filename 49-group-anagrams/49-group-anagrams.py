class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        
        for i in range(len(strs)):
            count = [0] * 26 
            for x in strs[i]:
                count[ord(x) - ord('a')] += 1
                
            ans[tuple(count)].append(strs[i])
        
        return ans.values()
            