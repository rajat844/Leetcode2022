class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int n = matrix.size();
        int m = matrix[0].size();
        
        int i = 0;
        int j = m-1;
        
        while(i < n && j > -1){
            if(matrix[i][j] == target) return true;
            else if(matrix[i][j] > target) j-= 1;
            else i += 1;
        }
        
        return false;
    }
};