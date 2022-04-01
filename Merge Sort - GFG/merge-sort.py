#User function Template for python3

class Solution:
    def merge(self,arr, l, m, r): 
        i = l
        j = m
        x = []
        while i <= m-1 and j <= r:
            if arr[i] > arr[j]:
                x.append(arr[j])
                j+=1
            else :
                x.append(arr[i])
                i+= 1
        while i <= m-1:
            x.append(arr[i])
            i+=1
        while j <= r:
            x.append(arr[j])
            j+=1
        u = 0
        for i in range(l,r+1):
            arr[i] = x[u]
            u += 1
        

        
        # code here
    def mergeSort(self,arr, low, high):
        #code here
            if low < high:
                mid = (low + high)//2
                self.mergeSort(arr,low, mid)
                self.mergeSort(arr,mid+1, high)

                self.merge(arr,low, mid+1, high)

#{ 
#  Driver Code Starts
#Initial Template for Python 3



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