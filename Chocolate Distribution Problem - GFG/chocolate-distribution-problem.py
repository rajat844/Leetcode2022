#User function Template for python3

class Solution:

    def findMinDiff(self,arr,n,m):
        arr.sort(reverse = True)
        
        mindif = arr[0] - arr[m-1]
        
        for i in range(1,len(arr) - m + 1 ):
            mindif = min(mindif,arr[i] - arr[i+m-1])
        return mindif

        # code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        N = int(input())
        A = [int(x) for x in input().split()]
        M = int(input())


        solObj = Solution()

        print(solObj.findMinDiff(A,N,M))
# } Driver Code Ends