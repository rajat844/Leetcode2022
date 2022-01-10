class Solution {
public:
    int cnt(vector<int> row, int mid){
        int low = 0; 
        int high = row.size() -1;
        int mid1;
        
        while(low<=high){
            mid1 = (low+high)/2;
            
            if(row[mid1] <= mid)low = mid1+1;
            else high = mid1-1;
        }
        return low;   
    }
    int kthSmallest(vector<vector<int>>& matrix, int k) {
        int n = matrix.size();
        int m = matrix[0].size();
        int l = matrix[0][0];
        int h = matrix[n-1][m-1];
        int mid;
        
        while(l<=h){
            int count = 0;
            int mid = (l+h)/2;
            
            for(int i = 0; i<n; i++){
                count += cnt(matrix[i],mid);
            }
            if (count >= k) h = mid-1;
            else l = mid+1;
        }
        return l;      
    }
};