#User function Template for python3

class Solution:
    def smallestpositive(self, array, n): 
        # Your code goes here  
        array.sort()
        target = 1
        s = 0
        for i in range(n):
            if array[i] <= target:
                s += array[i]
                target = s + 1
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