#User function Template for python3


# m is maximum of number zeroes allowed 
# to flip, n is size of array 
def findZeroes(arr, n, m) :
    # code here
    l = 0
    r = 0
    cnt = 0
    ans = 0
    
    while r < n:
        if arr[r] == 0:
            cnt += 1
            while cnt > m:
                if arr[l] == 0:
                    cnt -= 1
                l += 1
        ans = max(r-l+1,ans)
        r += 1
        
    return ans
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3




# Driver code 
if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int , input().strip().split()))
        m=int(input())
        ans= findZeroes(arr, n, m)
        print(ans)
        tc=tc-1
# } Driver Code Ends