class Solution {
public:
    int getSum(int a, int b) {
        while(b != 0){
            int temp = (uint32_t)(a & b) << 1;
            a = a ^ b;
            b = temp;
        }
        return a;
        
    }
};