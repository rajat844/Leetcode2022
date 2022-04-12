#User function Template for python3
class Solution:

	def printUnsorted(self,arr, n):
		# code here
		end = 0
		mn = arr[0]
		
		for i in range(1,n):
		    if mn > arr[i]:
		        end = i
		    else :
		        mn = arr[i]
		
		start = 0
		mx = arr[n-1]
		
		for i in range(n-2,-1,-1):
		    if mx < arr[i]:
		        start = i
		    else :
		        mx = arr[i]
		        
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