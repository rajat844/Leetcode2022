class Solution {
public:
    int robotSim(vector<int>& commands, vector<vector<int>>& obstacles) {
        vector<pair<int, int>> dir{{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        set<pair<int, int>> obs;

        for (int i = 0; i < obstacles.size(); i++) {
            obs.insert({obstacles[i][0], obstacles[i][1]});
        }

        int x = 0;
        int y = 0;
        int ans = 0;
        int d = 0;

        for (int i = 0; i < commands.size(); i++) {
            if (commands[i] == -1)
                d = (d + 1) % 4;
            else if (commands[i] == -2)
                d = (d + 3) % 4;

            else {
                int dx = dir[d].first;
                int dy = dir[d].second;
                for (int j = 0; j < commands[i]; j++) {
                    if (obs.find(make_pair(x + dx, y + dy)) != obs.end())
                        break;
                    else {
                        x += dx;
                        y += dy;
                    }
                }
                ans = max(ans, x * x + y * y);
            }
        }

        return ans;
    }
};