class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        vector<vector<int>> ans;
        
        for(int i = 0; i < nums.size() - 2; i++){
            int left = i + 1;
            int right = nums.size() - 1;
            
            while(left < right){
                int sum = nums[i] + nums[left] + nums[right];
                if(sum == 0) {
                    ans.push_back({nums[i],nums[left],nums[right]});
                    while(right > left && nums[right] == nums[right-1])
                        right--;
                    right--;
                     while(left < right && nums[left] == nums[left+1])
                        left++;
                    left++;                    
                }
                else if (sum > 0) {
                    while(right > left && nums[right] == nums[right-1])
                        right--;
                    right--;
                }
                else {
                    while(left < right && nums[left] == nums[left+1])
                        left++;
                    left++;
                }           
            }
            while(i < nums.size() - 2 && nums[i] == nums[i+1])
                i++;
        }
        return ans;      
        
    }
};