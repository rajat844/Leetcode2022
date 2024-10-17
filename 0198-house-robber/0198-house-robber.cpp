class Solution {
public:
    int helper(int i, vector<int> nums) {
        if(i >= nums.size()) return 0;
        
        int select = nums[i] + helper(i+2,nums);
        int unselect = helper(i+1,nums);
        
        return max(select,unselect);
    }
    
    int rob(vector<int>& nums) {
        int n = nums.size();
        
        vector<int> dp(n+2,0);
        
        for(int i = n-1; i >= 0; i--){
            int select = nums[i] + dp[i+2];
            int unselect = dp[i+1];
            dp[i] = max(select,unselect);
        }
        
        return dp[0];
    }
};