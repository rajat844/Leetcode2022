class Solution {
public:
    int houseRobber(vector<int> nums){
        int n = nums.size();
        
        vector<int> dp(n+2,0);
        
        for(int i = n-1; i >= 0; i--){
            int first = nums[i] + dp[i+2];
            int second = dp[i+1];
            dp[i] = max(first,second);
        }
        
        return dp[0];
    }
    
    int rob(vector<int>& nums) {
        vector<int> nums1;
        vector<int> nums2;
        
        
        for(int i = 0; i < nums.size(); i++){
            if(i == 0){
                nums1.push_back(nums[i]);
            }
            else if(i == nums.size() - 1){
                nums2.push_back(nums[i]);
            }
            else{
                nums1.push_back(nums[i]);
                nums2.push_back(nums[i]);
            }
        }
        return max(houseRobber(nums1),houseRobber(nums2));
        
        
    }
};