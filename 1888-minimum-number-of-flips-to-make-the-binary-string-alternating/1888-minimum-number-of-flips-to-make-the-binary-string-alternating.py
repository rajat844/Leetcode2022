import math
class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        s = s+s
        pssb1 = ""
        pssb2 = ""
        
        for i in range(len(s)):
            pssb1 += "0" if i%2==0 else "1"
            pssb2 += "1" if i%2==0 else "0"
        
        cnt1 = 0
        cnt2 = 0
        ans = math.inf
        l = 0
        for i in range(len(s)):
            if s[i] != pssb1[i]:
                cnt1 += 1
            if s[i] != pssb2[i]:
                cnt2 += 1
            
            if (i-l+1) > n:
                if pssb1[l] != s[l]:
                    cnt1 -= 1
                if pssb2[l] != s[l]:
                    cnt2 -= 1
                l += 1
            if i-l+1 == n:
                ans = min(cnt1,cnt2,ans)
        
        return ans
        
                
            