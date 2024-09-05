class Solution {
public:
    void getCombination(int idx,vector<int> temp,vector<vector<int>> &ans, int target, vector<int>& candidates){
        if(idx == candidates.size()){
            if(target == 0){
                ans.push_back(temp);
            }
            return;
        }
        
        if(target < 0) return;
        
        getCombination(idx+1,temp,ans,target,candidates);
        temp.push_back(candidates[idx]);
        target -= candidates[idx];
        getCombination(idx,temp,ans,target,candidates);
    }
    
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> ans;
        getCombination(0,{},ans,target,candidates);
        return ans;
    }
};