class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer,Integer> st = new HashMap<>();
        int[] ans = new int[2];
        
        for(int i = 0; i<nums.length; i++){
            int x = target-nums[i];
            if(st.containsKey(x)){
                ans[0] = i;
                ans[1] = st.get(x);
            }
            st.put(nums[i],i);
        }
        return ans;
    }
}