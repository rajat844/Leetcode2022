#User function Template for python3

class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        # code here
        st = []
        
        for i in range(n):
            st.append((start[i],end[i]))
            
        st = sorted(st, key = lambda x:x[1])
        
        curr = 0
        count = 0
        for i in range(n):
            if st[i][0] > curr:
                count += 1
                curr = st[i][1]
                
        return count

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        start = list(map(int,input().strip().split()))
        end = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.maximumMeetings(n,start,end))
# } Driver Code Ends