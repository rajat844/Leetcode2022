class Solution:
    def numberOfWeakCharacters(self, p: List[List[int]]) -> int:
        p.sort(key = lambda x : (x[0],-x[1]))
        st = []
        ans = 0
        
        for a,d in p:
            while len(st) > 0 and st[-1] < d:
                st.pop()
                ans += 1
            st.append(d)
        
        return ans
            
        