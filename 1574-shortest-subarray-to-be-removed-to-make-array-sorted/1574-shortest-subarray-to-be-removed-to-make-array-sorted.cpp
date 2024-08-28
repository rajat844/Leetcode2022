class Solution {
public:
    int findLengthOfShortestSubarray(vector<int>& arr) {
        int n = arr.size();
        
        int left = 0;
        while(left < n-1 && arr[left] <= arr[left+1]) left += 1;
        
        if(left == n-1) return 0;
        
        int right = n-1;
        while(right > left && arr[right] >= arr[right-1]) right -= 1;
        
        int ans = min(n-left-1,right);
        
        int i = 0;
        int j = right;
        
        while(i <= left && j < n){
            if(arr[i] <= arr[j]){
                ans = min(ans,j-i-1);
                i++;
            }
            else {
                j++;
            }
        }
        
        return ans;
        
        
    }
};