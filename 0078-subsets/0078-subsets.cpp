class Solution {
public:
    void generatePowerSet(int i, vector<int> nums, vector<int> st, vector<vector<int>> &ans){
        if(i == 0){
            ans.push_back(st);
            return;
        }
        generatePowerSet(i-1,nums,st,ans);
        st.push_back(nums[nums.size() - i]);
        generatePowerSet(i-1,nums,st,ans);
    }
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> ans;
        
        generatePowerSet(nums.size(),nums,{}, ans);
        return ans;
        
    }
};