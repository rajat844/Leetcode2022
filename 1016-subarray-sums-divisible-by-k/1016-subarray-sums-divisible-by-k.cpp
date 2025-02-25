class Solution {
public:
    int subarraysDivByK(vector<int>& nums, int k) {
        map<int,int> mp;
        mp[0] = 1;

        int sum = 0;
        int count = 0;

        for(int i = 0; i < nums.size(); i++){
            sum = (sum + nums[i]) % k;
            if(sum < 0) sum += k; 

            if(mp.find(sum) != mp.end()){
                count += mp[sum];
            }
            
            mp[sum] += 1;
        }

        return count;
    }
};