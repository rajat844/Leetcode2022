#Your task is to complete this function
#Your should return the required output
class Solution:
    def maxLen(self, n, arr):
        #Code here
        st = {}
        ans = 0
        currsum = 0
        
        for i in range(n):
            currsum += arr[i]
            
            if currsum == 0:
                ans = i + 1
            elif currsum in st:
                ans =max(ans,i- st[currsum])
            else:
                st[currsum] = i
        
        return ans
        
#{ 
#  Driver Code Starts
if __name__=='__main__':
    t= int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxLen(n ,arr))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends