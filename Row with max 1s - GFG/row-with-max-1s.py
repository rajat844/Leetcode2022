#User function Template for python3
class Solution:

	def rowWithMax1s(self,arr, n, m):
		# code here
		def count(nums):
		    l = 0
		    h = m-1
		    
		    while l <= h:
		        mid = (l+h) >> 1
		        if nums[mid] == 0:
		            l = mid + 1
		        else :
		            h = mid - 1
		    return m - l
		maxcount = 0
		rownumber = -1
		for i in range(n):
		    cnt = count(arr[i])
		    if cnt > maxcount:
		        maxcount = cnt
		        rownumber = i
		
		return rownumber

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, m = list(map(int, input().strip().split()))
        
        inputLine = list(map(int, input().strip().split()))
        arr = [[0 for j in range(m)] for i in range(n)]
        
        for i in range(n):
            for j in range(m):
                arr[i][j] = inputLine[i * m + j]
        ob = Solution()
        ans = ob.rowWithMax1s(arr, n, m)
        print(ans)
        tc -= 1

# } Driver Code Ends