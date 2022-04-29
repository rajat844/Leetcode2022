#User function Template for python3

class Solution:
    def merge(self,arr, l, m, r): 
        # code here
        temp = []
        start1 = l
        start2 = m
        
        while start1 < m and start2 <= r:
            if arr[start1] < arr[start2]:
                temp.append(arr[start1])
                start1 += 1
            else :
                temp.append(arr[start2])
                start2 += 1
        
        while start1 < m:
            temp.append(arr[start1])
            start1 += 1
        while start2 <= r:
            temp.append(arr[start2])
            start2 += 1
        
        a = 0
        for i in range(l,r+1):
            arr[i] = temp[a]
            a += 1
        
    def mergeSort(self,arr, l, r):
        #code here
        if l < r:
            mid = (l+r) >> 1
            self.mergeSort(arr,l,mid)
            self.mergeSort(arr,mid+1,r)
            
            self.merge(arr,l,mid+1,r)


#{ 
#  Driver Code Starts
#Initial Template for Python 3


import sys
input = sys.stdin.readline
if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        Solution().mergeSort(arr, 0, n-1)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends