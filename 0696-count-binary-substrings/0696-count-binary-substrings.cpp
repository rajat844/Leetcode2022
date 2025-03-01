class Solution {
public:
    int countBinarySubstrings(string s) {
        int cur = 1;
        int prev = 0;

        int ans = 0;

        for(int i = 1; i < s.size(); i++){
            if(s[i] == s[i-1]) cur += 1;
            else {
                prev = cur;
                cur  = 1;
            }
            if(prev >= cur) ans += 1;
        }

        return ans;
    }
};