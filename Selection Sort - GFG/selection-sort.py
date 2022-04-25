#User function Template for python3

class Solution:
    def selectionSort(self, arr,n):
        #code here
        for i in range(n):
            k = i
            for j in range(i,n):
                if arr[j] < arr[k]:
                    k = j
            arr[k],arr[i] = arr[i],arr[k]
            
        return arr

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends