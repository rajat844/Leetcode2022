class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xfffffff
        ans = 0
        while b != 0:
            s= (a ^ b) & mask
            carry = ((a & b) << 1) & mask
            
            a = s
            b = carry
        
        if (a > mask // 2):
            return ~(a ^ mask)
        return a
            
        