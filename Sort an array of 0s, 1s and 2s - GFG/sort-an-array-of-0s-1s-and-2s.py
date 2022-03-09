#User function Template for python3

class Solution:
    def sort012(self, arr, n):
        # code here
        st = -1
        mid = 0
        lst = n
        while mid < lst:
            if arr[mid] == 0:
                arr[mid], arr[st+1] = arr[st+1], arr[mid]
                mid += 1
                st += 1
            elif arr[mid] == 1:
                mid += 1
            elif arr[mid] == 2:
                arr[mid], arr[lst-1] = arr[lst-1], arr[mid]
                lst -= 1
        return arr

            
            
            


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends