class Solution {
public:
    int trap(vector<int>& height) {
        int maxLeft = INT_MIN;
        int maxRight = INT_MIN;

        int i = 0;
        int j = height.size() - 1;

        int ans = 0;

        while (i < j) {
            if (height[i] < height[j]) {
                if (height[i] >= maxLeft) maxLeft = height[i];
                else ans += maxLeft - height[i];
                i += 1;
            } else {
                if (height[j] >= maxRight) maxRight = height[j];
                else ans += maxRight - height[j];
                j -= 1;
            }
        }

        return ans;
    }
};