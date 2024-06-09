class Solution {
public:
    int reverse(int x) {
        int num = 0;
        while(x) {
            if (INT_MIN/10 > num || num > INT_MAX/10) return 0;
            num = num*10 + x%10;
            x /=10;            
        }
        return num;
    }
};