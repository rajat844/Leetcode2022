class Solution {
public:
    vector<int> rearrangeArray(vector<int>& nums) {
        int positiveIdx = 0;
        int negativeIdx = 1;
        
        vector<int> ans(nums.size());
        
        for(int i = 0; i < nums.size(); i++){
            if(nums[i] >= 0) {
                ans[positiveIdx] = nums[i];
                positiveIdx += 2;
            }
            else{
                ans[negativeIdx] = nums[i];
                negativeIdx += 2;
            }
        }
        
        return ans;
    }
};