class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        map<int,int> mp;

        int count = 0;
        mp[0] += 1;
        int sum = 0;

        for(int i = 0; i < nums.size(); i++){
            sum += nums[i];

            if(mp.find(sum - k) != mp.end()){
                count += mp[sum-k];
            }

            mp[sum] += 1;
        }

        return count;
    }
};