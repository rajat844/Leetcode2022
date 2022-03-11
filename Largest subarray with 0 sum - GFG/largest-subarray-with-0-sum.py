#Your task is to complete this function
#Your should return the required output
class Solution:
    def maxLen(self, n, arr):
        #Code here
        dic = {}
        ans = 0
        curr = 0
        
        for i in range(len(arr)):
            curr += arr[i]
            
            if curr == 0:
                temp_ans = i+1
                ans = max(temp_ans,ans)
            else:
                if curr not in dic:
                    dic[curr] = i+1
                else:
                    temp_ans = i-dic[curr] + 1
                    ans = max(temp_ans,ans)
                    
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