class Solution {
public:
    vector<int> singleNumber(vector<int>& nums) {
        //also check single number 2;
        long xorNumber = 0;
        
        for(int x : nums) xorNumber = xorNumber ^ x;
        
        long rightMostSetBit = xorNumber & (-xorNumber);
        
        
        int bucket1 = 0;
        int bucket2 = 0;
        
        for(int x : nums) {
            if((x & rightMostSetBit) == 0) bucket1 = bucket1 ^ x;
            else bucket2 = bucket2 ^ x;
        }
        
        return {bucket1,bucket2};
        
    }
};