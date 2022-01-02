class Solution {
public:
    int missingNumber(vector<int>& nums) {
        map<int,int> mp;
        
        for(int i = 0; i<nums.size();i++){
            mp[nums[i]]++;
        }
        
        for(int i = 0; i<=nums.size(); i++){
            if(mp.find(i) == mp.end()){ 
                return i;
                break;
            }
        }
        return -1;
        
    }
};