class Solution {
public:
    int countServers(vector<vector<int>>& grid) {
        int n = grid.size();
        int m = grid[0].size();

        vector<int> rowServer(n, 0);
        vector<int> colServer(m, 0);

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (grid[i][j] == 1) {
                    rowServer[i] += 1;
                    colServer[j] += 1;
                }
            }
        }

        int ans = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (grid[i][j] == 1 && (rowServer[i] > 1 || colServer[j] > 1)) {
                    ans += 1;
                }
            }
        }

        return ans;
    }
};