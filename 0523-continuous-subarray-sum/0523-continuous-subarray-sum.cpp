class Solution {
public:
    bool checkSubarraySum(vector<int>& nums, int k) {
        if(nums.size()<2) return false;
        int sum = 0;
        map<int,int> mp;
        mp[0] = -1;
        
        for(int i = 0; i < nums.size(); i++){
            sum += nums[i];
            int  diff = sum%k;
            if(mp.find(diff) != mp.end()){
                if(i - mp[diff] > 1) return true;
            } 
            else mp[diff] = i;
        }
        return false;
    }
};