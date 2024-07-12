class Solution {
public:
    int binarySearch(vector<int>& nums, int target,bool flag){
        int left = 0;
        int right = nums.size()-1;
        
        int res = -1;
        
        while(left <= right){
            int mid = (left + right) >> 1;
            if(nums[mid] == target){
                res = mid;
                if(flag == true) right = mid - 1;
                else left = mid + 1;
            }
            else if(nums[mid] > target){
                right = mid - 1;
            }
            else{
                left = mid + 1;
            }
        }
        
        return res;
    }
    vector<int> searchRange(vector<int>& nums, int target) {
        return{binarySearch(nums,target,true),binarySearch(nums,target,false)};
        
    }
};