#User function Template for python3

class Solution:
    #Function to sort a list using quick sort algorithm.
    def partition(self,arr,low,high):
        # code here
        pivot = arr[high]
        start = low - 1
        
        for i in range(low,high):
            if arr[i] <= pivot:
                start += 1
                arr[i],arr[start] = arr[start],arr[i]
                
        start += 1
        arr[start],arr[high] = arr[high],arr[start]
        return start
        
    def quickSort(self,arr,low,high):
        # code here
        if low < high:
            pi = self.partition(arr,low,high)
            
            self.quickSort(arr,low,pi-1)
            self.quickSort(arr,pi+1,high)
        
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        Solution().quickSort(arr,0,n-1)
        for i in range(n):
            print(arr[i],end=" ")
        print()

# } Driver Code Ends