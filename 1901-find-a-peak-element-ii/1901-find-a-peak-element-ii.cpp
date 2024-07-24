class Solution {
public:
    int maxEleIdx(vector<int>& arr){
        int mx = INT_MIN;
        int idx;
        
        for(int i = 0; i < arr.size(); i++){
            if(arr[i] > mx){
                idx = i;
                mx = arr[i];
            }
        }
        
        return idx;
    }
    vector<int> findPeakGrid(vector<vector<int>>& mat) {
        int left = 0;
        int right = mat.size() - 1;
        
        while(left <= right){
            int mid = (left + right) >> 1;
            int idx = maxEleIdx(mat[mid]);
            
            int l = (mid-1 >= 0) ? mat[mid-1][idx] : INT_MIN;
            int r = (mid+1 < mat.size()) ? mat[mid+1][idx] : INT_MIN;
            
            if(mat[mid][idx] > l && mat[mid][idx] > r) return {mid,idx};
            else if(mat[mid][idx] < r) left = mid + 1;
            else right = mid - 1;
        }
        
        return {};
        
    }
};