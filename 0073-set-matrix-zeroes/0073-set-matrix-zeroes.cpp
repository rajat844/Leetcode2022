class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        bool row0 = false;
        
        for(int i = 0; i < matrix.size(); i++){
            for(int j = 0; j < matrix[0].size(); j++){
                if(i == 0 && matrix[i][j] == 0){
                    row0 = true;
                    matrix[0][j] = 0;
                }
                else if(matrix[i][j] == 0){
                    matrix[i][0] = 0;
                    matrix[0][j] = 0;
                }
            }
        }
        
        for(int i = matrix.size()-1; i >= 1 ; i--){
            for(int j = matrix[0].size()-1; j >= 0; j--){
                if(matrix[i][0] == 0 || matrix[0][j] == 0)
                    matrix[i][j] = 0;
            }
        }
        
        for(int j = 0; j < matrix[0].size(); j++){
            if(row0) matrix[0][j] = 0;
        }
        
        
        
    }
};