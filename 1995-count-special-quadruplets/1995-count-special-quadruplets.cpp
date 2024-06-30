class Solution {
public:
    int countQuadruplets(vector<int>& nums) {
        //a + b + c = d
        //a + b = d - c
        
        map<int,int> mp;
        int len = nums.size();
        mp[nums[len-1]-nums[len-2]]++;
        int ans = 0;
        
        for(int b = len-3; b >= 1; b--){
            for(int a = b-1; a >= 0; a--){
                ans += mp[nums[a] + nums[b]];
            }
            
            for(int d = len-1; d > b;d--){
                mp[nums[d] - nums[b]]++;
            }
        }
        
        return ans;
        
    }
};