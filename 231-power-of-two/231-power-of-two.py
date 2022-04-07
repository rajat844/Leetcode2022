class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        
        while n > 1 and n & 1 == 0:
            n = n >> 1
        
        if n == 1:
            return True
        return False
        