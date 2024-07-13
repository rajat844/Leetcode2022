class Solution {
public:
    bool search(vector<int>& nums, int target) {
        bool found = false;
        int left = 0;
        int right = nums.size() - 1;
        
        while(left <= right){
            while (left < right && nums[left] == nums[left+1]) left++;
            while (left < right && nums[right] == nums[right-1]) right--;
            int mid = (left + right) >> 1;
            
            if(nums[mid] == target) return true;
            
            else if(nums[left] <= nums[mid]){
                if(nums[left] <= target && nums[mid] >= target) right = mid - 1;
                else left = mid + 1;
            }
            else {
                if(nums[mid] <= target && nums[right] >= target) left = mid + 1;
                else right = mid - 1;
            }
        }
        
        return false;
        
    }
};