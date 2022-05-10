class Solution:
    def numDecodings(self, s: str) -> int:
        
        if s[0] == "0":
            return 0
        prev2 = 1
        prev = 9 if s[0] =="*" else 1
        
        for i in range(2,len(s) + 1):
            first = s[i-2]
            second = s[i-1]
            curr = 0
            
            if second == "*":
                curr += 9*prev
            elif second > "0":
                curr += prev
            
            
            if first == "*":
                if second == "*":
                    curr += 15*prev2
                elif second <= "6":
                    curr += 2*prev2
                else:
                    curr += prev2
                    
            elif first == "1":
                if second == "*":
                    curr += 9*prev2
                else:
                    curr += prev2
                    
            elif first == "2":
                if second == "*":
                    curr += 6*prev2
                elif second <= "6":
                    curr += prev2
                    
            prev2 = prev
            prev = curr
            
        
        return prev % (10**9 + 7)
                