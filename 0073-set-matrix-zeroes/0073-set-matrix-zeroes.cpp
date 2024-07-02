class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        int row0 = false;
        
        for(int i = 0; i < matrix.size(); i++){
            for(int j = 0; j < matrix[0].size(); j++){
                if(i == 0 && matrix[i][j] == 0){
                    row0 = true;
                }
                else if(matrix[i][j] == 0){
                    matrix[i][0] = 0;
                    matrix[0][j] = 0;
                }
            }
        }
        
        for(int i = matrix.size()-1; i > 0; i--){
            for(int j = matrix[0].size()-1; j >= 0; j--){
                if(matrix[i][0] == 0 || matrix[0][j] == 0) 
                    matrix[i][j] = 0;
            }
        }
        
        if(row0 == true){
            for(int j = 0; j < matrix[0].size(); j++){
                matrix[0][j] = 0;
            }
        }
    }
};