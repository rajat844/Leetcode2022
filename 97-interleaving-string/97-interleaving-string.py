class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        def recursion(i,first,second):
            if dp[i][first][second] != None:
                return dp[i][first][second]
            if first == len(s1):
                return s3[i:] == s2[second:]
            if second == len(s2):
                return s3[i:] == s1[first:]
            
            if s1[first] == s3[i] and s2[second] == s3[i]:
                dp[i][first][second] = recursion(i+1,first+1,second) or recursion(i+1,first,second+1)
                return dp[i][first][second]
            elif s1[first] == s3[i]:
                dp[i][first][second] = recursion(i+1,first+1,second)
                return dp[i][first][second]
            elif s2[second] == s3[i]:
                dp[i][first][second] = recursion(i+1,first,second+1)
                return dp[i][first][second]
            else:
                dp[i][first][second] =  False
                return dp[i][first][second]
        
        dp = [[[None for i in range(len(s2)+1)]for j in range(len(s1)+1)]for k in range(len(s3)+1)]
        if len(s1) + len(s2) != len(s3):
            return False
        return recursion(0,0,0)
                
        
        
            