#User function Template for python3

class Solution:
    def nQueen(self, n):
        # code here
        ans = []
        board = [[0 for i in range(n)]for j in range(n)]
        def check(row,col):
            rt = row
            ct = col
            
            while rt >= 0 and ct >= 0:
                if board[rt][ct] == 1:
                    return False
                rt -= 1
                ct -= 1
            
            rt = row
            ct = col
            
            while ct >= 0:
                if board[rt][ct] == 1:
                    return False
                ct -= 1
            
            rt = row
            ct = col
            
            while ct >= 0 and rt < n:
                if board[rt][ct] == 1:
                    return False
                ct -= 1
                rt += 1
            
            return True
            
            
            
        def helper(col,s):
            if col == n:
                ans.append(s[::])
                return 
            
            for row in range(n):
                if check(row,col):
                    board[row][col] = 1
                    s.append(row+1)
                    helper(col+1,s)
                    s.pop()
                    board[row][col] = 0
                    
        helper(0,[])
        return ans
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        ob = Solution()
        ans = ob.nQueen(n)
        if(len(ans) == 0):
            print("-1")
        else:
            for i in range(len(ans)):
                print("[",end="")
                for j in range(len(ans[i])):
                    print(ans[i][j],end = " ")
                print("]",end = " ")
            print()
                
# } Driver Code Ends