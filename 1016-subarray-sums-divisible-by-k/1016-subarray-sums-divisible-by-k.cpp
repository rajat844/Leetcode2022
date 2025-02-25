class Solution {
public:
    int subarraysDivByK(vector<int>& nums, int k) {
        vector<int> mp(k,0);
        mp[0] = 1;

        int sum = 0;
        int count = 0;

        for(int i = 0; i < nums.size(); i++){
            sum = (sum + nums[i]) % k;
            if(sum < 0) sum += k; 

            count += mp[sum];

            mp[sum] += 1;
        }

        return count;
    }
};