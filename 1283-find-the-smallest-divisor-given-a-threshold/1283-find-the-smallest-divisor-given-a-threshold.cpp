class Solution {
public:
    bool isLess(vector<int> &nums,int threshold, int divisor){
        for(int x:nums){
            int temp = x/divisor;
            if(x % divisor != 0) temp += 1;
            threshold -= temp;
        }
        if(threshold >= 0) return true;
        return false;
    }
    int smallestDivisor(vector<int>& nums, int threshold) {
        int left = 1;
        int right = INT_MIN;
        
        for(int x: nums){
            right = max(x,right);
        }
        
        int ans;
        
        while(left <= right){
            int mid = (left + right) >> 1;
            
            if(isLess(nums,threshold,mid)){
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