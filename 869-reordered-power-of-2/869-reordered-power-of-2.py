class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        def countDigits(num):
            arr = [0 for u in range(10)]
            while num:
                arr[num%10] += 1
                num = num//10
            
            return arr
        
        cnt = countDigits(n)
        y = 1
        for i in range(31):
            if cnt == countDigits(y):
                return True
            y = y << 1
        
        return False
        