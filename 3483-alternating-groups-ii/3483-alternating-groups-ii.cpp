class Solution {
public:
    int numberOfAlternatingGroups(vector<int>& colors, int k) {
        int ans = 0;
        int n = colors.size();

        int i = 0;

        for (int j = 1; j < (n + k - 1); j++) {
            if (colors[j % n] != colors[(j - 1) % n]) {
                if (j - i + 1 == k) {
                    ans += 1;
                    i += 1;
                }
            } else {
                i = j;
            }
        }


        return ans;
    }
};