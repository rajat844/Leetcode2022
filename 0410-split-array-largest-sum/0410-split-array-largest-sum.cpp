class Solution {
public:
    bool isPossible(vector<int>& nums, int k, int maxSum){
        int curr = 0;
        for(int x : nums){
            if(x > maxSum) return false;
            if(curr + x > maxSum){
                k--;
                curr = x;
            }
            else{
                curr += x;
            }
        }
        k--;
        if(k >= 0) return true;
        return false;
    }
    int splitArray(vector<int>& nums, int k) {
        if(nums.size() < k) return -1;
        
        int left = 0;
        int right = 0;
        int ans;
        
        for(int x: nums){
            right += x;
        }
        
        while(left <= right){
            int mid = (left + right) >> 1;
            
            if(isPossible(nums,k,mid)){
                ans = mid;
                right = mid - 1;
            }
            else{
                left = mid + 1;
            }
        }
        
        return ans;
    }
};