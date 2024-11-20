class Solution {
public:
    int minFallingPathSum(vector<vector<int>>& matrix) {
        int n = matrix.size();
        int m = matrix[n-1].size();
        vector<vector<int>> dp(n,vector<int>(m,0));
        
        for(int i = 0; i < m; i++){
            dp[n-1][i] = matrix[n-1][i];
        }
        
        for(int depth = n-2; depth >= 0; depth--){
            for(int idx = 0; idx < m; idx++){
                int sum;
                if(idx == 0)
                    sum = min(dp[depth+1][idx],dp[depth+1][idx+1]);
                else if (idx == m-1)
                    sum = min(dp[depth+1][idx],dp[depth+1][idx-1]);
                else
                    sum = min(dp[depth+1][idx],min(dp[depth+1][idx+1],dp[depth+1][idx-1]));
                
                dp[depth][idx] =  sum + matrix[depth][idx]; 
            }
        }
        
        int ans = INT_MAX;
        
        for(int x : dp[0]){
            ans = min(x,ans);
        }
        
        return ans;
        
    }
};