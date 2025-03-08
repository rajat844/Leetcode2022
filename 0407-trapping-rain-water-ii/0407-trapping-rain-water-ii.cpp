class Solution {
private:
    struct Comp {
        bool operator()(tuple<int, int, int>& a, tuple<int, int, int>& b) {
            return get<0>(a) > get<0>(b);
        }
    };

public:
    int trapRainWater(vector<vector<int>> & heightMap) {
        int n = heightMap.size();
        int m = heightMap[0].size();

        vector<vector<bool>> visited(n, vector<bool>(m, false));
        priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, Comp>
            q;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (i == 0 || i == n - 1 || j == 0 || j == m - 1) {
                    q.push({heightMap[i][j], i, j});
                    visited[i][j] = true;
                }
            }
        }

        vector<vector<int>> neigh = {{0, 1}, {1, 0}, {-1, 0}, {0, -1}};

        int ans = 0;
        int maxHeight = -1;

        while (!q.empty()) {
            auto [h, r, c] = q.top();
            maxHeight = max(maxHeight, h);
            ans += maxHeight - h;

            q.pop();

            for (int i = 0; i < 4; i++) {
                int dr = r + neigh[i][0];
                int dc = c + neigh[i][1];

                if (dr < n && dr >= 0 && dc >= 0 && dc < m &&
                    visited[dr][dc] == false) {
                    visited[dr][dc] = true;
                    q.push({heightMap[dr][dc], dr, dc});
                }
            }
        }

        return ans;
    }
};