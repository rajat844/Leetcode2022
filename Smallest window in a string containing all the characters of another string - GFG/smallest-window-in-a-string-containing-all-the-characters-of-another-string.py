#User function Template for python3

from collections import defaultdict
class Solution:
    
    #Function to find the smallest window in the string s consisting
    #of all the characters of string p.
    def smallestWindow(self, s, p):
        #code here
        st = defaultdict(int)
        
        for ch in p:
            st[ch] += 1
        
        cnt = len(st)
        
        l = 0
        ans = ""
        cnt1 = 0
        
        for r in range(len(s)):
            st[s[r]] -= 1
            if st[s[r]] == 0:
                cnt1 += 1
            
            while cnt1 == cnt and l <= r:
                if ans == "" or len(ans) > r-l+1:
                    ans = s[l:r+1]
                st[s[l]] += 1
                if st[s[l]] == 1:
                    cnt1 -= 1
                l += 1
        
        return ans if len(ans) > 0 else -1
                        
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        s=str(input())
        p=str(input())
        ob = Solution()
        print(ob.smallestWindow(s,p))
# } Driver Code Ends