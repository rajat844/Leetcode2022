class Solution {
    // public int minSteps(int[] nums,int currPos){
    //     if (currPos >= nums.length-1){
    //         return 0;
    //     }
    //     int maxJumps = nums[currPos];
    //     int minPossible = Integer.MAX_VALUE;
    //     for(int i= 1; i<maxJumps+1; i++){
    //          minPossible = Math.min(minPossible,1+minSteps(nums,i+currPos));
    //     }
    //     return minPossible;
    // }
    public int jump(int[] nums) {
        int len = nums.length;
        int[] dp = new int[len];
        dp[len-1] = 0;
        
        for(int i = len-2; i >= 0 ;i--){
            int x = nums[i];
            int ans = Integer.MAX_VALUE-1;
            for(int j = i+1;j < i+x+1; j++){
                if (j >= len) continue;
                ans = Math.min(ans,dp[j] + 1);
            }
            dp[i] = ans;
        }
        return dp[0];
        
    }
}