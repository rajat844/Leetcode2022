class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> ans;
        int n = nums.size();
        
        int subsets = (1 << n);
        
        for(int i = 0; i < subsets; i++){
            int x = i;
            int j = 0;
            vector<int> temp;
            while(x){
                if((x & 1) != 0) temp.push_back(nums[j]);
                j += 1;
                x = (x >> 1);
            }
            ans.push_back(temp);
        }
        
        return ans;
        
    }
};