class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def valid(i,j):
            row = i
            column = j
            
            while row >= 0 and column >= 0:
                if s[row][column] == "Q":
                    return False
                row -= 1
                column -= 1
            
            row = i
            column = j
            
            while column >= 0:
                if s[row][column] == "Q":
                    return False
                column -= 1
            
            column = j
            
            while column >= 0 and row < n:
                if s[row][column] == "Q":
                    return False
                column -= 1
                row += 1
            
            return True
            
        def helper(j):
            if j == n:
                tempans = [''.join(x) for x in s] 
                ans.append(tempans)
                return 
            
            for i in range(n):
                if valid(i,j):
                    s[i][j] = "Q"
                    helper(j+1)
                    s[i][j] = "."
                    
        ans = []
        s = [["." for i in range(n)]for j in range(n)]
        helper(0)
        return ans
                    
        