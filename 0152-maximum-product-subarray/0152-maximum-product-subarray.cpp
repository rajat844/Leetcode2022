class Solution {
public:
    int maxProduct(vector<int>& nums) {
        long long mx = INT_MIN;
        long long  prefix = 1;
        long long suffix = 1;
        for(int i=0; i<nums.size(); i++) {
            if(prefix == 0) prefix = 1;
            if(suffix == 0) suffix = 1;
            if(prefix*10 < INT_MAX) prefix = prefix * nums[i];
            if(suffix*10 < INT_MAX) suffix = suffix * nums[nums.size()-i-1];
            mx = max(mx, max(prefix, suffix));
        }
        return (int)mx;
    }
};