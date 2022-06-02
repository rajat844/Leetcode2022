#User function Template for python3

class Solution:
    def smallestpositive(self, arr, n): 
        # Your code goes here  
        arr.sort()
        s = 0
        target = 1
        
        for i in range(n):
            if arr[i] <= target:
                s += arr[i]
                target = s+1
            else:
                break
        
        return target

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        array = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.smallestpositive(array,n))


# } Driver Code Ends