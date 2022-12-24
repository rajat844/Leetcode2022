class Solution {
    public int removeDuplicates(int[] nums) {
        int curr = -101;
        int l = 0;
        
        for(int i = 0; i<nums.length; i++){
            if(curr != nums[i]){
                curr = nums[i];
                nums[l] = curr;
                l += 1;
            }
        }
        return l;
        
        
    }
}