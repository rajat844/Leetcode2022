class Solution {
public:
    void combination(int k,int n, vector<vector<int>> &ans,vector<int> temp,int prev){
        if(k == 0){
            if(n == 0){
                ans.push_back(temp);
            }
            return;
        }
        
        if(n < 0) return;

        for(int i = prev+1; i <= 9; i++){
            temp.push_back(i);
            n -= i;
            combination(k-1,n,ans,temp,i);
            temp.pop_back();
            n += i;            
        }
    }
    
    vector<vector<int>> combinationSum3(int k, int n) {
        vector<vector<int>> ans;
        
        combination(k,n,ans,{},0);
        return ans;
    }
};