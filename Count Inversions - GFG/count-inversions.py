class Solution:
    #User function Template for python3
    
    # arr[]: Input Array
    # N : Size of the Array arr[]
    #Function to count inversions in the array.

    def inversionCount(self, arr, n):
        # Your Code Here
        def merge(start,mid,end):
            nonlocal ans
            st = []
            i = start
            j = mid
            
            while i < mid and j <= end:
                if arr[i] <= arr[j]:
                    st.append(arr[i])
                    i += 1
                else:
                    st.append(arr[j])
                    j += 1
                    ans += mid - i
            while i < mid :
                st.append(arr[i])
                i += 1
            while j <= end:
                st.append(arr[j])
                j += 1
            
            a = 0
            for i in range(start,end+1):
                arr[i] = st[a]
                a += 1
            
        def mergeSort(start,end):
            if start < end :
                mid = (start + end)//2
                mergeSort(start,mid)
                mergeSort(mid+1,end)
                
                merge(start,mid+1,end)
        ans = 0
        mergeSort(0,n-1)
        return ans

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
    for tt in range(t):
        n = int(input())
        a = list(map(int, input().strip().split()))
        obj = Solution()
        print(obj.inversionCount(a,n))
# } Driver Code Ends