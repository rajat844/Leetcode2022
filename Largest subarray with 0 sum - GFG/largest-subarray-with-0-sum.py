#Your task is to complete this function
#Your should return the required output
class Solution:
    def maxLen(self, n, arr):
        #Code here
        dic = {}
        ans = 0
        sumnow = 0
        for i in range(n):
            sumnow += arr[i]
            
            if sumnow == 0:
                temp = i+1
                ans = max(temp,ans)
            else:
                if sumnow in dic:
                    temp = i - dic[sumnow] + 1
                    ans = max(temp,ans)
                else :
                    dic[sumnow] = i+1
                    
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