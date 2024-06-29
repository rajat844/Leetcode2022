class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        int cnt1 = 0;
        int ele1 = NULL;
        int cnt2 = 0;
        int ele2 = NULL;
        
        for(int i = 0; i < nums.size(); i++){
            if(cnt1 == 0 && nums[i] != ele2){
                ele1 = nums[i];
                cnt1++;
            }
            else if(cnt2 == 0 && nums[i] != ele1){
                ele2 = nums[i];
                cnt2++;
            }
            else if(ele1 == nums[i]){
                cnt1++;
            }
            else if(ele2 == nums[i]){
                cnt2++;
            }
            else{
                cnt1--;
                cnt2--;
            }
        }
        
        cnt1 = 0, cnt2 = 0;
        for(int i = 0; i < nums.size(); i++){
            if(ele1 == nums[i]) cnt1++;
            if(ele2 == nums[i]) cnt2++;
        }
        
        vector<int> ans;
        if(cnt1 > nums.size()/3) ans.push_back(ele1);
        if(cnt2 > nums.size()/3 && ele1 != ele2) ans.push_back(ele2);
        return ans;
    }
};