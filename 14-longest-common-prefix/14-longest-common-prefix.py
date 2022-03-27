class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ''
        
        s = strs[0]
        
        for j in range(len(s)):
            for i in range(len(strs)):
                if j == len(strs[i]) or strs[i][j] != s[j]:
                    return  ans
            ans += s[j] 
            
        return ans