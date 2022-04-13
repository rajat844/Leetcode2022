class Solution:
    def sortString(self, s: str) -> str:
        arr = [0] * 26
        
        for i in range(len(s)):
            arr[ord(s[i]) - ord('a')] += 1
            
        ans = ''
        while max(arr) > 0 :
            for i in range(len(arr)):
                if arr[i] > 0:
                    arr[i] -= 1
                    ans += chr(i + 97)
            
            for i in range(len(arr) - 1 , -1,-1):
                if arr[i] > 0:
                    arr[i] -= 1
                    ans += chr( 97 + i)
        
        return ans
            
        
        