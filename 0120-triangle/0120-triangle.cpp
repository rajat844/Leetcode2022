class Solution {
public:
    int helper(vector<vector<int>> &triangle, int depth, int idx){
        if(depth == triangle.size()) return 0;
        if(idx >= triangle[depth].size() || idx < 0) return 0;
        
        int sum = min(helper(triangle,depth+1,idx),helper(triangle,depth+1,idx+1));
        return sum + triangle[depth][idx];
        
    }
    int minimumTotal(vector<vector<int>>& triangle) {
        int n = triangle.size();
        int m = triangle[n-1].size();
        vector<vector<int>> dp(n,vector<int>(m,0));
        
        for(int i = 0; i < m; i++){
            dp[n-1][i] = triangle[n-1][i];
        }
        
        for(int depth = n-2; depth >= 0; depth--){
            for(int idx = 0; idx < triangle[depth].size(); idx++){
                int sum = min(dp[depth+1][idx],dp[depth+1][idx+1]);
                dp[depth][idx] =  sum + triangle[depth][idx]; 
            }
        }
        
        return dp[0][0];
        
    }
};