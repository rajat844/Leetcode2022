class Solution {
public:
    int minimumRecolors(string blocks, int k) {
        int count = 0;

        int i = 0;
        int j = 0;

        while (j - i < k) {
            if (blocks[j] == 'W')
                count += 1;
            j += 1;
        }
        int ans = count;

        while (i < blocks.size() && j < blocks.size()) {
            if (blocks[j] == 'W')
                count += 1;
            if (blocks[i] == 'W')
                count -= 1;
            i += 1;
            j += 1;

            ans = min(ans, count);
        }

        return ans;
    }
};