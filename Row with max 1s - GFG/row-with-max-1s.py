#User function Template for python3
class Solution:

	def rowWithMax1s(self,arr, n, m):
	    def helper(currarr):
	        x = len(currarr)
	        l = 0
	        h = len(currarr) - 1
	        
	        while l <= h:
	            mid = (l+h)//2
	            
	            if currarr[mid] == 1 and (currarr[mid - 1] == 0 or mid == 0):
	                return x - mid
	            elif currarr[mid] == 1:
	               h = mid - 1
	            else:
	               l = mid + 1
	       
	        return -1
		
		
		tillnow = 0
		rownum = -1
		for i in range(len(arr)):
		    x = helper(arr[i])
		    if x > tillnow:
		        tillnow = x
		        rownum = i
		return rownum 
		    

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