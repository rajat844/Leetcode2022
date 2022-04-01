#User function Template for python3
class Solution:

	def findMaximum(self,arr, n):
		# code here
		l = 0
		h = n-1
		
		while l < h:
		    mid = (l+h)//2
		    if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
		        return arr[mid]
		    elif arr[mid] > arr[l] and arr[mid] < arr[mid + 1]:
		        l = mid
		    else:
		        h = mid
		
		return arr[n-1]

#{ 
#  Driver Code Starts
#Initial Template for Python 3





if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMaximum(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends