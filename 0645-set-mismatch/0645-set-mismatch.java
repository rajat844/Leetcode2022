class Solution {
    public int[] findErrorNums(int[] nums) {
        int modFactor = nums.length + 1;
        for(int i = 0; i< nums.length; i++){
            int x = nums[i] % modFactor;
            nums[x-1] += modFactor;
        }
        int[] ans = new int[2];
        for(int i = 0; i< nums.length; i++){
            if (nums[i] / modFactor > 1) ans[0] = i+1;
            if (nums[i] / modFactor < 1) ans[1] = i+1;
        }
        
        return ans;
        
    }
}