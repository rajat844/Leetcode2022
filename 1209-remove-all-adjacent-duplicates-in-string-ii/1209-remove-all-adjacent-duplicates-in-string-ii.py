class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        st = []
        
        for char in s:
            if len(st) > 0 and st[-1][0] == char:
                if st[-1][1] == k - 1:
                    for x in range(k-1):
                        st.pop()
                else:
                    st.append((char,st[-1][1] + 1))
            
            else:
                st.append((char,1))
                
        ans = ''
        for i in range(len(st)):
            ans += st[i][0]
        
        return ans