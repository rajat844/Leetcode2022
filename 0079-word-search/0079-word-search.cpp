class Solution {
public:
    bool isExist(vector<vector<char>> &board, vector<vector<int>> &visited, string word,int i, int j, int idx){
        if(idx == word.size()) return true;
        
        if(i >= board.size() || j >= board[0].size()) return false;
        
        if(board[i][j] == word[idx] && visited[i][j] != 1){
            visited[i][j] = 1;
            
            bool case1 = isExist(board,visited,word,i+1,j,idx+1);
            bool case2 = isExist(board,visited,word,i,j+1,idx+1);
            bool case3 = isExist(board,visited,word,i-1,j,idx+1);
            bool case4 = isExist(board,visited,word,i,j-1,idx+1);
            
            if(case1 || case2 || case3 || case4) return true;
            
            visited[i][j] = 0;
        }
        
        return false;        
    }
    
    bool exist(vector<vector<char>>& board, string word) {
        int n = board.size();
        int m = board[0].size();
        
        vector<vector<int>> visited (n, vector<int> (m,0));
        
        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                if(board[i][j] == word[0]){
                    if(isExist(board,visited,word,i,j,0)) return true;
                }
            }
        }
        return false;
    }
};