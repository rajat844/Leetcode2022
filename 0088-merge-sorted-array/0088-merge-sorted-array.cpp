class Solution {
public:
    void merge(vector<int>& nums1, int n, vector<int>& nums2, int m) {
        int lastEle = n+m-1;
        int i = n-1;
        int j = m-1;
        
        while(j >= 0){
            if(i >= 0 and nums1[i] > nums2[j])
                nums1[lastEle--] = nums1[i--];
            else 
                nums1[lastEle--] = nums2[j--];
        }
    }
        
};