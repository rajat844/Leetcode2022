class Solution:
    def sortString(self, s: str) -> str:
        arr = [0 for i in range(26)]
        
        for i in range(len(s)):
            arr[ ord(s[i]) - ord('a')] += 1
            
        ans = ''
        while max(arr) > 0:
            for i in range(26):
                if arr[i] > 0:
                    arr[i] -= 1
                    ans += chr(97+i)
            
            for i in range(25,-1,-1):
                if arr[i] > 0:
                    arr[i] -= 1
                    ans += chr(97+i)
                    
        return ans