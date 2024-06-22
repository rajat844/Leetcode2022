class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int ele = nums[0];
        int count = 1;
        
        for(int i = 0; i < nums.size(); i++){
            if(ele == nums[i]) count += 1;
            else{
                count -= 1;
                if(count == 0) {
                    ele = nums[i];
                    count = 1;
                    }
            }
        }
        
        return ele;
    }
};