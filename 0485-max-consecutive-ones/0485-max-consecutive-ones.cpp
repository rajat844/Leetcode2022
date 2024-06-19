class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int count_max = 0;
        int temp_max = 0;
        
        for(int i = 0; i < nums.size(); i++){
            if(nums[i] == 1) {
                temp_max++;
                count_max = max(temp_max,count_max);
            }
            else{
                temp_max = 0;
            }
        }
        
        return count_max;
        
    }
};