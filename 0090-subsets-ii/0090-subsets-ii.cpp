class Solution {
public:
    void getSubsets(int idx, vector<vector<int>> &ans, vector<int> temp, vector<int> &nums){
        if(idx == nums.size()){
            ans.push_back(temp);
            return;
        }
        
        temp.push_back(nums[idx]);
        getSubsets(idx+1,ans,temp,nums);
        
        temp.pop_back();
        while(idx < nums.size() - 1 && nums[idx] == nums[idx+1]) idx++;
        getSubsets(idx+1,ans,temp,nums);
        
    }
    
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        
        vector<vector<int>> ans;
        getSubsets(0,ans,{},nums);
        return ans;      
    }
};