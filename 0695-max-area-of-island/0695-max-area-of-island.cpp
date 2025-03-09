class Solution {

    int getMaxArea(int i, int j, vector<vector<int>>& grid,
                   vector<vector<int>>& dir) {
        queue<pair<int, int>> q;
        int n = grid.size();
        int m = grid[0].size();

        int area = 1;
        q.push({i, j});
        grid[i][j] = 0;

        while (!q.empty()) {
            int r = q.front().first;
            int c = q.front().second;
            q.pop();

            for (int x = 0; x < 4; x++) {
                int dr = r + dir[x][0];
                int dc = c + dir[x][1];

                if (dr >= 0 && dr < n && dc >= 0 && dc < m &&
                    grid[dr][dc] == 1) {
                    area += 1;
                    q.push({dr, dc});
                    grid[dr][dc] = 0;
                }
            }
        }

        return area;
    }

public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        vector<vector<int>> dir = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        int ans = 0;
        for (int i = 0; i < grid.size(); i++) {
            for (int j = 0; j < grid[0].size(); j++) {
                if (grid[i][j] == 1) {
                    ans = max(ans, getMaxArea(i, j, grid, dir));
                }
            }
        }

        return ans;
    }
};