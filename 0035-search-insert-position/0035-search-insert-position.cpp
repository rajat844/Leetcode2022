class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int l = 0;
        int r = nums.size()-1;
        int insertIdx = nums.size();
        
        while(l <= r){
            int mid = (l+r) >> 1;
            
            if(nums[mid] == target) return mid;
            else if(nums[mid] > target){
                insertIdx = mid;
                r = mid - 1;
            }
            else{
                l = mid + 1;
            }
        }
        
        return insertIdx;
        
    }
};