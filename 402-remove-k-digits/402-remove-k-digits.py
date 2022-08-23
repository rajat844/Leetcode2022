class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        st = []
        for i in range(len(num)):
            while len(st) > 0 and int(st[-1]) > int(num[i]) and k > 0:
                st.pop()
                k -= 1
            st.append(num[i])
        
        st = st[:len(st) - k]
        ans = "".join(st)
        
        return str(int(ans)) if ans else "0"
        