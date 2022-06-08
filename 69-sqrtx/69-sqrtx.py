class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        h = x
        
        while l <= h:
            mid = (l+h) >> 1
            if mid*mid == x:
                return mid
            elif mid * mid > x:
                h = mid -1
            else :
                l = mid + 1
        
        if l * l > x :
            return h
        else :
            return l
        
        