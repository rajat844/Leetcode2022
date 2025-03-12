class Solution {
public:
    int maximumCount(vector<int>& nums) {
        int left = 0;
        int right = nums.size() - 1;

        while (left <= right) {
            int mid = (left + right) >> 1;
            cout << mid;

            if (nums[mid] >= 0) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        int neg = right + 1;
        left = 0;
        right = nums.size() - 1;

        while (left <= right) {
            int mid = (left + right) >> 1;

            if (nums[mid] > 0) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        int pos = nums.size() - left;

        return max(pos, neg);
    }
};