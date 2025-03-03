class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int ones = 0;
        int twos = 0;

        for(int i =0; i < nums.size(); i++){
            ones = (ones ^ nums[i]) & (~twos);
            twos = (twos ^ nums[i]) & (~ones);
        }

        return ones;
    }
};

//  first occ = ! two
// second occ =  present in ones


// first -> add it to ones. 
// second -> add it to two, remove it from ones
// third -> remove it from two


// o -> ^ 