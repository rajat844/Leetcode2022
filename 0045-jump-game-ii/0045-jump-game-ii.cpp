class Solution {
public:
    int jump(vector<int>& nums) {
        int ans = 0;
        int left = 0;
        int right = 0;        
        
        while(right < nums.size() - 1){
            int righttemp = right;
            for(int i = left; i <= right; i++){
                righttemp = max(righttemp, i + nums[i]);
            }
            ans += 1;
            left = right + 1;
            right = righttemp;            
        }
        
        return ans;
        
    }
};