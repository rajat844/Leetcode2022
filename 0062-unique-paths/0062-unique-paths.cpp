class Solution {
public:
    int helper(int i, int j,int n, int m){
        if(i == n && j == m) return 1;
        if(i <= n && j <= m){
            int first = helper(i+1,j,n,m);
            int second = helper(i,j+1,n,m);
            return first + second;
        }
        else{
            return 0;
        }
    }
    int uniquePaths(int m, int n) {
        vector<vector<int>> dp(n,vector<int>(m,1));
        
        for(int i = 1; i < n; i++){
            for(int j = 1; j < m; j++){
                dp[i][j] = dp[i][j-1] + dp[i-1][j];
            }
        }
        
        return dp[n-1][m-1];
        
    }
};