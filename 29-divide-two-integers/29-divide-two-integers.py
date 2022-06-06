class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        positive = (dividend < 0) == (divisor < 0)
        dividend, divisor = abs(dividend) ,abs(divisor)
        
        ans = 0
        
        while dividend >= divisor:
            temp = divisor
            i = 1
            while dividend >= temp:
                dividend -= temp
                ans += i
                i = i << 1
                temp = temp << 1
        
        if not positive:
            ans = -ans
        
        return min(max(-2147483648,ans),2147483647)
        
        