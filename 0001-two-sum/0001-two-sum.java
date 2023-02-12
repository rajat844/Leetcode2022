class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer,Integer> st = new HashMap<>();
        
        for(int i = 0; i < nums.length; i++){
            if(st.containsKey(target-nums[i])){
                return new int[] {st.get(target-nums[i]),i};
            }
            st.put(nums[i],i);
        }
        
        return new int[]{-1,-1};
        
    }
}