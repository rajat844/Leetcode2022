class Solution {
    struct Comp {
        bool operator()(tuple<int, int, int>& a, tuple<int, int, int>& b) {
            return get<0>(a) > get<0>(b);
        }
    };

public:
    vector<vector<int>> highestPeak(vector<vector<int>>& isWater) {
        int n = isWater.size();
        int m = isWater[0].size();

        vector<vector<int>> heights(n, vector<int>(m, -1));
        priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, Comp>
            q;
        vector<vector<int>> dir = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (isWater[i][j] == 1) {
                    heights[i][j] = 0;
                    q.push({0, i, j});
                }
            }
        }

        while (!q.empty()) {
            int h = get<0>(q.top());
            int r = get<1>(q.top());
            int c = get<2>(q.top());
            q.pop();

            for (int i = 0; i < 4; i++) {
                int dr = r + dir[i][0];
                int dc = c + dir[i][1];

                if (dr >= 0 && dr < n && dc >= 0 && dc < m &&
                    heights[dr][dc] == -1) {
                    heights[dr][dc] = h + 1;
                    q.push({h + 1, dr, dc});
                }
            }
        }

        return heights;
    }
};