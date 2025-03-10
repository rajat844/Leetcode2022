class Solution {
public:
    int atMostK(vector<int>& nums, int k) {
        map<int, int> intCount;
        int ans = 0;

        int left = 0;

        for (int right = 0; right < nums.size(); right++) {
            if (k == 0)
                return 0;
            intCount[nums[right]] += 1;

            while (intCount.size() > k) {
                intCount[nums[left]] -= 1;
                if (intCount[nums[left]] == 0) {
                    intCount.erase(nums[left]);
                }
                left += 1;
            }

            if (intCount.size() <= k) {
                ans += right - left + 1;
            }
        }
        return ans;
    }
    int subarraysWithKDistinct(vector<int>& nums, int k) {
        return atMostK(nums, k) - atMostK(nums, k - 1);
    }
};