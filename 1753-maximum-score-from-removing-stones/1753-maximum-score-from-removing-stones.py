class Solution:
    def maximumScore(self, x: int, y: int, z: int) -> int:
        a = max(x,y,z)
        c = min(z,y,z)
        b = x+y+z-a-c
        
        if a >= b+c:
            return b+c
        else:
            return a + ((b+c-a)//2)
        