#User function Template for python3

class Solution:
    def median(self, matrix, r, c):
        def helper(arr,k):
            l = 0
            h = len(arr)-1
        
            while l <= h:
                mid = (l+h)>>1
            
                if arr[mid]<= k:
                    l = mid +1
                else :
                    h = mid -1
        
            return l
        
    	#code here 
    	l = 1
    	h = 2000
    	

    	while l <= h:
    	    mid = (l+h)>>1
    	    
    	    count = 0
    	    for i in range(r):
    	        count += helper(matrix[i],mid)
    	    
    	    if count <= (r*c)//2:
    	        l = mid+1
    	    else :
    	        h = mid - 1
    	
    	return l
    	        
    	    
    	

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        r,c = map(int,input().strip().split())
        matrix = [[0 for j in range(c)] for i in range(r)]
        line1 = [int(x) for x in input().strip().split()]       
        k = 0
        for i in range(r):
            for j in range (c):
                matrix[i][j]=line1[k]
                k+=1
        ans = ob.median(matrix, r, c);
        print(ans)
# } Driver Code Ends