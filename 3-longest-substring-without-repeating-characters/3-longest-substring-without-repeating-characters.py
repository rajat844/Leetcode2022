class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st = {}
        n = len(s)
        count = 0
        start = 0
        
        for i in range(n):
            if s[i] in st and st[s[i]] >= start:
                start = st[s[i]] + 1
            else:
                tempcount = i - start + 1
                count = max(tempcount,count)
            st[s[i]] = i
        return count
                
            
        '''
        {
        a = 0
        
        }
        
        
        
        '''