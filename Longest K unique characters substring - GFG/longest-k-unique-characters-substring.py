#User function Template for python3
from collections import defaultdict
class Solution:

    def longestKSubstr(self, s, k):
        # code here
        mp = defaultdict(int)
        n = len(s)
        ans = 0
        i = 0
        j = 0
        while i < n:
            mp[s[i]] += 1
            if len(mp) < k:
                i += 1
            elif len(mp) == k:
                i += 1
                ans = max(ans,i-j)
            else:
                while len(mp) > k:
                    mp[s[j]] -= 1
                    if mp[s[j]] == 0:
                        del mp[s[j]]
                    j += 1
                i += 1
        return -1 if ans == 0 else ans
                        
                
                
            
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()
        k = int(input())

        solObj = Solution()

        ans = solObj.longestKSubstr(s, k)

        print(ans)

# } Driver Code Ends