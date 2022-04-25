#Sort the array using insertion sort

class Solution:
    def insertionSort(self, alist, n):
        for i in range(n):
            x = arr[i]
            j = i-1
            while j > -1 and arr[j] > x:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = x
        
        return arr
                
        #code here

#{ 
#  Driver Code Starts
if __name__=="__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
    
        Solution().insertionSort(arr,n)
    
        for i in range(n):
            print(arr[i],end=" ")
    
        print()
# } Driver Code Ends