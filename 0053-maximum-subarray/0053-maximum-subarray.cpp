class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int maxSum = INT_MIN;
        int currSum = 0;
        int start = 0;
        int end = 0;
        
        for(int i = 0; i < nums.size(); i++){
            if(currSum < 0){
                start = i;
                currSum = 0;
            }
            currSum += nums[i];
            if(currSum > maxSum){
                maxSum = currSum;
                end = i;
            }
        }
        
        for(int i = start; i <= end; i++){
            cout << nums[i] << ",";  
        }
        cout << endl;
        
        return maxSum;
        
    }
};