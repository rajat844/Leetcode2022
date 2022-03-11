class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1.0
        nn = n
        if nn < 0:
            nn *= -1
        while nn > 0:
            if nn % 2 == 0:
                x = x*x
                nn = nn/2
            else :
                ans = x* ans
                nn = nn -1 
        
        if n < 0 :
            ans = 1/ans
        
        return ans
        