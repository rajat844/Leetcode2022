class Solution {
public:
    bool isSafe(vector<string>& board,int n, int col, int row){       
        int x = col -1;
        
        while(x >= 0){
            if(board[row][x] == 'Q') return false;
            x--;
        }
        
        x = col-1;
        int y = row-1;
        int z = row + 1;
        
        while(x >= 0){
            if(y >= 0 && board[y][x] == 'Q') return false;
            if(z < n && board[z][x] == 'Q') return false;
            x--;
            y--;
            z++;
        }
        return true;
        
    }
    
    void NQueens(int col, int n, vector<vector<string>> &ans,vector<string> &board){
        if(col == n){
            ans.push_back(board);
        }
        
        for(int row = 0; row < n; row++){
            if(isSafe(board,n,col,row)){
                board[row][col] = 'Q';
                NQueens(col+1,n,ans,board);
                board[row][col] = '.';
            }
        }
    }
    
    vector<vector<string>> solveNQueens(int n) {
        vector<vector<string>> ans;
        
        vector<string> board(n);
        string s(n,'.');
        
        for(int i = 0; i < n; i++){
            board[i] = (s);
        }
        
        NQueens(0,n,ans,board);
        return ans;
    }
};