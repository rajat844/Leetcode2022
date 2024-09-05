class Solution {
public:
    void getCombination(int idx, int target, vector<int> &candidates, vector<vector<int>> &ans,vector<int> temp){
        if(idx == candidates.size()){
            if(target == 0){
                ans.push_back(temp);
            }
            return;
        }
        
        if(target < 0) return;
        
        temp.push_back(candidates[idx]);
        target -= candidates[idx];
        getCombination(idx+1,target,candidates, ans, temp);
        
        temp.pop_back();
        target += candidates[idx];
        
        while(idx < candidates.size() - 1 && candidates[idx] == candidates[idx+1]) idx++;
        getCombination(idx+1,target,candidates, ans, temp);
        
    }
    
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        sort(candidates.begin(),candidates.end());
        
        vector<vector<int>> ans;
        getCombination(0,target,candidates,ans,{});
        return ans;
    }
};