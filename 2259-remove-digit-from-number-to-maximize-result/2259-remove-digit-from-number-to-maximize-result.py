class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        diff = -math.inf
        ans = None
        
        for i in range(1,len(number)):
            if number[i-1] == digit:
                if number[i] > number[i-1]:
                    return number[:i-1]+number[i:]
                else:
                    last = i - 1
        
        if number[-1] == digit:
            last = len(number) - 1
        
        return number[:last] + number[last+1:]
        