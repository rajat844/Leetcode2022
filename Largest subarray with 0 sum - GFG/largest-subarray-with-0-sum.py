#Your task is to complete this function
#Your should return the required output
class Solution:
    def maxLen(self, n, arr):
        #Code here
        dic = {}
        sumnow = 0
        maxi = 0
        
        for i in range(n):
            sumnow += arr[i]
            
            if sumnow == 0:
                maxi = i+1
            elif sumnow in dic:
                maxi = max(maxi,i-dic[sumnow])
            else:
                dic[sumnow] = i
        
        return maxi
            
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