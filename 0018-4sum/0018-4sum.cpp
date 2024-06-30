class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        
        sort(nums.begin(),nums.end());
        vector<vector<int>> ans;
        if(nums.size() < 4) return ans;
        
        for(int i = 0; i < nums.size() - 3; i++){
            for(int j = i+1; j < nums.size() - 2; j++){
                int left = j+1;
                int right = nums.size() - 1;
                while(left < right){
                    long long newTarget = (long long)target - (long long)nums[i] - (long long)nums[j];
                    if(newTarget == nums[left] + nums[right]){
                        ans.push_back({nums[i],nums[j],nums[left],nums[right]});
                        while(left < right && nums[left] == nums[left+1])
                            left++;
                        left++;
                        while(right > left && nums[right] == nums[right-1])
                            right--;
                        right--;
                    }
                    else if(nums[left] + nums[right] > newTarget){
                        while(right > left && nums[right] == nums[right-1])
                            right--;
                        right--;
                    }
                    else{
                      while(left < right && nums[left] == nums[left+1])
                            left++;
                        left++;  
                    }
                    
                }
                while(j < nums.size() - 2 && nums[j] == nums[j+1])
                    j++;
            }
            while(i < nums.size() - 3 && nums[i] == nums[i+1])
                i++;
        }
        return ans;
    }
};