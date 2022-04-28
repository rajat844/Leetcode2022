#User function Template for python3
class Solution:

	def printUnsorted(self,arr, n):
		# code here
		mx = arr[0]
		end = 0
		for i in range(n):
		    if arr[i] < mx:
		        end = i
		    else :
		        mx = arr[i]
		        
		mn = arr[-1]
		start = 0
		for i in range(n-1,-1,-1):
		    if arr[i] > mn:
		        start = i
		    else :
		        mn = arr[i]
		        
		return [start,end]
#{ 
#  Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.printUnsorted(arr, n)
        print(str(ans[0]) + " " + str(ans[1]))
        tc -= 1

# } Driver Code Ends