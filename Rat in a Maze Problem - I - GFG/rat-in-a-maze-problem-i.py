#User function Template for python3

class Solution:
    def findPath(self, m, n):
        # code here
        ans = []
        def helper(row ,col,s):
            if row == n-1 and col == n-1:
                ans.append(s[::])
                return 
            
            m[row][col] = 0
            if row+1 < n and m[row+1][col] == 1:
                s += "D"
                helper(row+1,col,s)
                s = s[:-1]
            if row - 1 >= 0 and m[row-1][col] == 1:
                s += "U"
                helper(row-1,col,s)
                s = s[:-1]
            if col+1 < n and m[row][col+1] == 1:
                s += "R"
                helper(row,col+1,s)
                s = s[:-1]
            if col -1 >= 0 and m[row][col-1] == 1:
                s+= "L"
                helper(row,col-1,s)
                s = s[:-1]
            m[row][col] = 1
            
        if m[0][0] == 1:
            helper(0,0,"")
        return ans
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        
        matrix = [[0 for i in range(n[0])]for j in range(n[0])]
        k=0
        for i in range(n[0]):
            for j in range(n[0]):
                matrix[i][j] = arr[k]
                k+=1
        ob = Solution()
        result = ob.findPath(matrix, n[0])
        result.sort()
        if len(result) == 0 :
            print(-1)
        else:
            for x in result:
                print(x,end = " ")
            print()
# } Driver Code Ends