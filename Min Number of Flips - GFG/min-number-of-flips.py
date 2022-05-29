#User function Template for python3


class Solution:
    def minFlips(self, s):
        # Code here
        cnt1 = 0
        cnt2 = 0
        
        for i in range(len(s)):
            if i % 2 == 0:
                if s[i] == "0":
                    cnt1 += 1
                else:
                    cnt2 += 1
            else:
                if s[i] == "1":
                    cnt1 += 1
                else :
                    cnt2 += 1
        
        return min(cnt1,cnt2)
                
        


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for i in range(t):
        S=input()
        Obj=Solution()
        ans=Obj.minFlips(S)
        print(ans)
# } Driver Code Ends