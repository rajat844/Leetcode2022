class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        if(nums2.size() < nums1.size()) return findMedianSortedArrays(nums2,nums1);
        
        int n = nums1.size();
        int m = nums2.size();
        
        int left = 0;
        int right = n;
        
        int d = (n + m + 1) >> 1;
        
        while(left <= right){
            int cut1 = (left + right) >> 1;
            int cut2 = d - cut1;
            
            int l1 = (cut1 > 0) ? nums1[cut1-1] : INT_MIN;
            int l2 = (cut2 > 0) ? nums2[cut2-1] : INT_MIN;
            
            int r1 = (cut1 < n) ? nums1[cut1] : INT_MAX;
            int r2 = (cut2 < m) ? nums2[cut2] : INT_MAX;
            
            if(l1 <= r2 && l2 <= r1){
                if((n+m) % 2 == 1) return max(l1,l2);
                return (max(l1,l2) + min(r1,r2))/2.0;
            }
            
            else if (l1 > r2) right = cut1 - 1;
            else left = cut1 + 1;
        }
        return -1;        
    }
};