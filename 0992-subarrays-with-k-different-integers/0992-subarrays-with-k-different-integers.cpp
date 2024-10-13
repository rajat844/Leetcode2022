class Solution {
public: 
    int helper(vector<int> & nums, int k){
        if(k == 0) return 0;
        int start = 0;
        map<int,int> mp;
        int ans = 0;
        
        for(int i = 0; i < nums.size(); i++){
            mp[nums[i]] += 1;
            
            while(mp.size() > k){
                mp[nums[start]] -= 1;
                if(mp[nums[start]] == 0){
                    mp.erase(nums[start]);
                }
                start += 1;
            }
            
            if(mp.size() <= k){
                ans += i - start + 1;
            }  
        }
        
        return ans;
    }
    
    int subarraysWithKDistinct(vector<int>& nums, int k) {
        return helper(nums,k) - helper(nums,k-1);
    }
};