#User function Template for python3

class Solution:
    def cutRod(self, price, n):
        #code here
        length = [i+1 for i in range(n)]
        st = [[-1 for i in range(n+1)]for j in range(n+1)]
        
        # def helper(n,l):
        #     if n == 0 or l== 0:
        #         st[n][l] = 0
                
        #     if st[n][l] != -1:
        #         return st[n][l]
        #     else :
        #         if l >= n :
        #             st[n][l] = max(helper(n-1,l),price[n-1] + helper(n,l-length[n-1]))
        #             return st[n][l]
        #         else :
        #             st[n][l] = helper(n-1,l)
        #             return st[n][l]
        
        
        # helper(n,n)
        
        for i in range(n+1):
            for j in range(n+1):
                if i == 0 or j == 0:
                    st[i][j] = 0
                elif (j >= length[i-1]):
                    st[i][j] = max(st[i-1][j],price[i-1] + st[i][j-length[i-1]])
                else :
                    st[i][j] = st[i-1][j]
                
        return st[n][n]

#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.cutRod(a, n))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends