class Solution {
public:
    int numberOfSubarrays(vector<int>& nums, int k) {
        map<int,int> mp;
        int ans = 0;
        int count = 0;
        mp[0] = 1;
        
        for(int i = 0; i < nums.size(); i++){
            if(nums[i] % 2) count += 1;
            
            int x = count - k;
            
            if(mp.find(x) != mp.end()){
                ans += mp[x];
            }
            mp[count]+= 1;
        }
        return ans;
        
    }
};