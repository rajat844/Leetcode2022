class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 0 :
            return False
        if n == 0:
            return False
        x = math.log(n)/math.log(4)
        
        if math.floor(x) == math.ceil(x):
            return True
        return False
        