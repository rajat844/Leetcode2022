class Solution {
public:
    void getCombination(vector<vector<int>> &ans, int i, int target,vector<int> st, vector<int> candidates){
        if(i == candidates.size()){
            if(target == 0){
                ans.push_back(st);
            }
            return;            
        }
        
        if(target < 0) return;
        
        getCombination(ans,i+1,target,st,candidates);
        st.push_back(candidates[i]);
        target -= candidates[i];
        getCombination(ans,i,target,st,candidates);
    }
    
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> ans;
        getCombination(ans,0,target,{},candidates);
        return ans;
        
    }
};