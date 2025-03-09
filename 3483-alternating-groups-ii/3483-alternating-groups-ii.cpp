class Solution {
public:
    int numberOfAlternatingGroups(vector<int>& colors, int k) {
        int ans = 0;
        int n = colors.size();

        int i = 0;
        int j = 1;

        while (i < n + k - 1 && j < n + k - 1) {
            if (colors[j % n] != colors[(j - 1) % n]) {
                j += 1;
                if (j - i == k) {
                    ans += 1;
                    i += 1;
                }
            } else {
                i = j;
                j = j + 1;
            }
        }

        return ans;
    }
};