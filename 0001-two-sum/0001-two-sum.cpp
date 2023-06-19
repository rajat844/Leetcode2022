class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> ans;
        unordered_map<int,int> st;
        
        for (int i = 0; i < nums.size(); i++){
            int diff = target - nums[i];
            
            if(st.find(diff) != st.end()) {
                ans.push_back(i);
                ans.push_back(st[diff]);
                break;
            }
            else {
                st[nums[i]] = i;
            }
        }
        return ans;
        
    }
};