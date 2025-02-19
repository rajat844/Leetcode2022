class Solution {
public:
    string getHappyString(int n, int k) {
        int possible = 3 * pow(2, n - 1);

        if (k > possible || n == 0)
            return "";

        vector<char> options{'a', 'b', 'c'};

        map<char, vector<char>> mp{
            {'a', {'b', 'c'}}, {'b', {'a', 'c'}}, {'c', {'a', 'b'}}};

        int left = 1;
        int right = possible; 

        string ans = "";

        for (int i = 0; i < n; i++) {
            int curr = left;
            int partition = (right - left + 1) / options.size();

            for (char x : options) {
                if (k >= curr && k < curr + partition) {
                    ans += x;
                    left = curr;
                    right = curr + partition;
                    options = mp[x];
                }
                curr += partition;
            }
        }

        return ans;
    }
};