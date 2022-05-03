class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        div = 1
        
        while x >= 10*div:
            div = 10*div
            
        while x :
            first = x//div
            last = x%10
            
            if first != last:
                return False
            
            x = x%div
            x = x//10
            
            div = div//100
        
        return True
            