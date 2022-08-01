class Solution:
    def isHappy(self, n: int) -> bool:
        st = set()
        while n != 1 and n not in st:
            st.add(n)
            s = 0
            while n:
                s += (n%10) ** 2
                n = n//10
            n = s
        
        if n == 1:
            return True
        return False
                
                
        