class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        maxSt = [0 for i in range(26)]
        st = [0 for i in range(26)]
        
        for word in words2:
            for ch in word:
                st[ord(ch) - ord("a")] += 1
            
            for i in range(26):
                maxSt[i] = max(maxSt[i],st[i])
                st[i] = 0

                
        ans = []
        for word in words1:
            curr = True
            for ch in word:
                st[ord(ch) - ord('a')] += 1
                
            for i in range(26):
                if st[i] < maxSt[i]:
                    curr = False
                    break
   
            if curr == True:
                ans.append(word)
                
            st = [0 for i in range(26)]
            
        return ans
            
                