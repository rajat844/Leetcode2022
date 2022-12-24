class Solution {
    public void reverse(int l, int h,int[] nums){
        while(l<h){
            int temp = nums[l];
            nums[l] = nums[h];
            nums[h] = temp;
            l += 1;
            h -= 1;
            
        }
    }
    public void rotate(int[] nums, int k) {
        int n = nums.length;
        k %= n;
        reverse(0,n-1,nums);
        reverse(0,k-1,nums);
        reverse(k,n-1,nums);      
    }
}