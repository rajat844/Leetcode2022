class Solution:
    #User function Template for python3
    
    # arr[]: Input Array
    # N : Size of the Array arr[]
    #Function to count inversions in the array.
    def inversionCount(self, arr, n):
        # Your Code Here
        def merge(low,mid,high):
            inver = 0
            i = low
            j = mid
            
            temp = []
            
            while i <= mid -1  and j <= high :
                if arr[i] <= arr[j]:
                    temp.append(arr[i])
                    i += 1
                else :
                    temp.append(arr[j])
                    j += 1
                    inver += mid - i
            
            while i<= mid-1:
                temp.append(arr[i])
                i += 1
            while j<= high:
                temp.append(arr[j])
                j += 1
            
            a = 0
            for i in range(low,high+1):
                arr[i] = temp[a]
                a += 1
            
            return inver
                
        
        def mergeSort(low,high):
            inver = 0
            if low < high:
                mid = (low + high)//2
                inver += mergeSort(low,mid)
                inver += mergeSort(mid+1,high)
                
                inver += merge(low,mid+1,high)
            
            return inver
            
        return mergeSort(0,len(arr) - 1)

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