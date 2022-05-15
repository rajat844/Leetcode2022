class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        ans = []
        prev = ""
        for i in range(len(words)):
            x = ''.join(sorted(words[i]))
            if prev != x:
                ans.append(words[i])
                prev = x
                
        return ans
        