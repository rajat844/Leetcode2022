#User function Template for python3

class Solution:
    def shouldPunish (self, roll, marks, n, avg):
        #  your code here
        count = 0
        for i in range(n):
            for j in range(n-i-1):
                if roll[j] > roll[j+1]:
                    count += 2
                    roll[j],roll[j + 1] = roll[j+1],roll[j]
        s = (sum(marks) - count)
        
        if s/n > avg:
            return 1
        return 0
#{ 
#  Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range (t):
    n, avg = input ().split ()
    n = int (n)
    avg = float (avg)
    roll = list(map(int, input().split()))
    marks = list(map(int, input().split()))
    ob=Solution()
    print (ob.shouldPunish (roll, marks, n, avg))
# } Driver Code Ends