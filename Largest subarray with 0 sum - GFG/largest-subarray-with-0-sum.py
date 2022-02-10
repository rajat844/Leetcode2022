#Your task is to complete this function
#Your should return the required output
class Solution:
    def maxLen(self, n, arr):
        #Code here
        
        d = {}
        s = 0
        ans = 0
        
        for i in range(len(arr)):
            s = s + arr[i]
            
            if s == 0:
                ans = i+1
            
            if s != 0:
                if s not in d:
                    d[s] = i+1
                else :
                    ans = max(ans,i-d[s] +1)
                    
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