#User function Template for python3

class Solution:
    
    #Function to find the maximum number of activities that can
    #be performed by a single person.
    def activitySelection(self,n,start,end):
        # code here
        st = []
        for i in range(len(start)):
            st.append((start[i],end[i]))
        
        st.sort(key = lambda x: x[1])
        ans = 0
        day = 0
        
        for i in range(n):
            if st[i][0] > day:
                day = st[i][1]
                ans += 1
        
        return ans
                

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        start = list(map(int,input().strip().split()))
        end = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.activitySelection(n,start,end))
# } Driver Code Ends