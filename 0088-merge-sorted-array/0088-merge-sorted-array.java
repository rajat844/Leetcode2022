class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int i = n-1;
        int j = m-1;
        int k = m+n-1;
        
        while (i >= 0 && j >= 0){
            if(nums2[i] > nums1[j]){
                nums1[k] = nums2[i];
                i -= 1;
                k -= 1;
            }
            else{
                nums1[k] = nums1[j];
                j -= 1;
                k -= 1;
            }
        }
        
        while(i >= 0){
            nums1[k] = nums2[i];
            k -= 1;
            i -= 1;
        }
    }
}