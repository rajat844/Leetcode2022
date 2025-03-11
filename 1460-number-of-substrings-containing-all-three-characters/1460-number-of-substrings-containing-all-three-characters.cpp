class Solution {
public:
    int numberOfSubstrings(string s) {
        int n = s.size();
        vector<int> arr(3, 0);
        int count = 0;
        int ans = 0;
        int left = 0;

        for (int right = 0; right < s.size(); right++) {
            arr[s[right] - 'a']++;
            if (arr[s[right] - 'a'] == 1)
                count += 1;

            while (count == 3) {
                ans += n - right;
                arr[s[left] - 'a']--;
                if (arr[s[left] - 'a'] == 0)
                    count -= 1;
                left += 1;
            }
        }

        return ans;
    }
};