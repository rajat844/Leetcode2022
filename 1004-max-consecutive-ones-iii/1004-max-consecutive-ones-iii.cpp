class Solution {
public:
    int longestOnes(vector<int>& nums, int k) {
        //max length of subarray with atmost k zeros
        
        int ans = 0;
        
        int i = 0;
        int j = 0;
        
        while(i < nums.size() && j < nums.size()){
            if(nums[i] == 1){
                i++;
            }
            else if(nums[i] == 0 && k > 0){
                k--;
                i++;
            }
            else{
                if(nums[j] == 0){
                    k++;
                }
                j++;
            }
            ans = max(ans,i-j);
        }
        return ans;
    }
};