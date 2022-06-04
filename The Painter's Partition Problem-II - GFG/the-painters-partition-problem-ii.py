#User function Template for python3

class Solution:
    def minTime (self, arr, n, k):
        #code here
        def ifPossible(x):
            target = 1
            temp = 0
            for i in range(n):
                temp += arr[i]
                if temp > x:
                    temp = arr[i]
                    target += 1
                    if target > k or temp > x:
                        return False
            return True
                    
                
        h = sum(arr)
        l = max(arr)
        ans = 0
        while l <= h:
            mid = (l+h) >> 1
            if ifPossible(mid):
                h = mid - 1
            else :
                l = mid + 1
        
        return l
                
            
                
            
            
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        str = input().split()
        k = int(str[0])
        n = int(str[1])
        arr = input().split()
        for itr in range(n):
            arr[itr] = int(arr[itr])

        ob = Solution()
        print(ob.minTime(arr,n,k))
# } Driver Code Ends