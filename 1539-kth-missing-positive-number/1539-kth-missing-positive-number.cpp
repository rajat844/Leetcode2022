class Solution {
public:
    int findKthPositive(vector<int>& arr, int k) {
        for(int x : arr){
            if(x <= k) k++;
            else break;
        }
        
        return k;
        
//         int left = 0;
//         int right = arr.size() - 1;
        
//         while (left <= right){
//             int mid = (left + right) >> 1;
            
//             if (arr[mid] - mid - 1 < k) left = mid + 1;
//             else right = mid - 1;
//         }
        
//         return left + k;
        
    }
};