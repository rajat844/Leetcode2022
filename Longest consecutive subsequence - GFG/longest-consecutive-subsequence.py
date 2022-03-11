 #User function Template for python3
 
class Solution:
    
    # arr[] : the input array
    # N : size of the array arr[]
    
    #Function to return length of longest subsequence of consecutive integers.
    def findLongestConseqSubseq(self,nums, N):
        #code here
        dic = {}
        maxcount = 0
        for i in range(len(nums)):
            dic[nums[i]] = i
        
        for i in range(len(nums)):
            if nums[i] - 1 in dic:
                continue
            else :
                count = 0
                x = nums[i]
                while x in dic:
                    count += 1
                    x += 1
                maxcount = max(count,maxcount)
        return maxcount     

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

if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        n=int(input())
        a = list(map(int, input().strip().split()))
        print(Solution().findLongestConseqSubseq(a,n))
# } Driver Code Ends