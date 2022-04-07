class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n != 0 :
            if n % 2 == 1:
                ans += 1
            n = n >> 1
        
        return ans